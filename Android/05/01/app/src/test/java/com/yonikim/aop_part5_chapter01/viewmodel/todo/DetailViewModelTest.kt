package com.yonikim.aop_part5_chapter01.viewmodel.todo

import com.yonikim.aop_part5_chapter01.ViewModelTest
import com.yonikim.aop_part5_chapter01.data.entity.ToDoEntity
import com.yonikim.aop_part5_chapter01.domain.todo.InsertToDoItemUseCase
import com.yonikim.aop_part5_chapter01.presentation.detail.DetailMode
import com.yonikim.aop_part5_chapter01.presentation.detail.DetailViewModel
import com.yonikim.aop_part5_chapter01.presentation.detail.ToDoDetailState
import com.yonikim.aop_part5_chapter01.presentation.list.ListViewModel
import com.yonikim.aop_part5_chapter01.presentation.list.ToDoListState
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.test.runBlockingTest
import org.junit.Before
import org.junit.Test
import org.koin.core.parameter.parametersOf
import org.koin.test.inject

/**
 * [DetailViewModel] 을 테스트하기 위한 Unit Test Class
 * 1. initData()
 * 2. test viewModel fetch
 * 3. test Todo Delete
 * 4. test Todo Update
 */
@ExperimentalCoroutinesApi
internal class DetailViewModelTest : ViewModelTest() {

    private val id = 1L

    private val listViewModel by inject<ListViewModel>()
    private val detailViewModel by inject<DetailViewModel> { parametersOf(DetailMode.DETAIL, id) }


    private val insertToDoItemUseCase: InsertToDoItemUseCase by inject()

    private val todo = ToDoEntity(
        id = id,
        title = "title $id",
        description = "description $id",
        hasCompleted = false
    )

    @Before
    fun init() {
        initData()
    }

    private fun initData() = runBlockingTest {
        insertToDoItemUseCase(todo)
    }

    @Test
    fun `test viewModel fetch`() = runBlockingTest {
        val detailTestObservable = detailViewModel.toDoDetailLiveData.test()
        detailViewModel.fetchData()

        detailTestObservable.assertValueSequence(
            listOf(
                ToDoDetailState.UnInitialized,
                ToDoDetailState.Loading,
                ToDoDetailState.Success(todo)
            )
        )
    }

    @Test
    fun `test Todo Delete`() = runBlockingTest {
        val detailTestObservable = detailViewModel.toDoDetailLiveData.test()
        detailViewModel.deleteToDoItem()

        detailTestObservable.assertValueSequence(
            listOf(
                ToDoDetailState.UnInitialized,
                ToDoDetailState.Loading,
                ToDoDetailState.Delete
            )
        )

        val listTestObservable = listViewModel.todoListLiveData.test()
        listViewModel.fetchData()
        listTestObservable.assertValueSequence(
            listOf(
                ToDoListState.UnInitialized,
                ToDoListState.Loading,
                ToDoListState.Success(listOf())
            )
        )
    }

    @Test
    fun `test Todo Update`() = runBlockingTest {
        val detailTestObservable = detailViewModel.toDoDetailLiveData.test()
        val updateTitle = "title 1 update"
        val updateDescription = "description 1 update"

        val updateToDoItem = todo.copy(
            title = updateTitle,
            description = updateDescription
        )

        detailViewModel.writeToDoItem(
            title = updateTitle,
            description = updateDescription
        )

        detailTestObservable.assertValueSequence(
            listOf(
                ToDoDetailState.UnInitialized,
                ToDoDetailState.Loading,
                ToDoDetailState.Success(updateToDoItem)
            )
        )
    }

}