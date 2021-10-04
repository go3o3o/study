package com.yonikim.aop_part5_chapter01.viewmodel.todo

import com.yonikim.aop_part5_chapter01.ViewModelTest
import com.yonikim.aop_part5_chapter01.data.entity.ToDoEntity
import com.yonikim.aop_part5_chapter01.presentation.detail.DetailMode
import com.yonikim.aop_part5_chapter01.presentation.detail.DetailViewModel
import com.yonikim.aop_part5_chapter01.presentation.detail.ToDoDetailState
import com.yonikim.aop_part5_chapter01.presentation.list.ListViewModel
import com.yonikim.aop_part5_chapter01.presentation.list.ToDoListState
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.test.runBlockingTest
import org.junit.Test
import org.koin.core.parameter.parametersOf
import org.koin.test.inject

/**
 * [DetailViewModel] 을 테스트하기 위한 Unit Test Class
 * 1. test viewModel fetch
 * 2. test Todo Insert
 */
@ExperimentalCoroutinesApi
internal class DetailViewModelForWriteTest : ViewModelTest() {

    private val detailViewModel: DetailViewModel by inject { parametersOf(DetailMode.WRITE, id) }
    private val listViewModel: ListViewModel by inject()

    private val id = 0L

    private val todo = ToDoEntity(
        id,
        title = "title 1",
        description = "description 1",
        hasCompleted = false
    )

    @Test
    fun `test viewModel fetch`() = runBlockingTest {
        val detailTestObservable = detailViewModel.toDoDetailLiveData.test()

        detailViewModel.fetchData()
        detailTestObservable.assertValueSequence(
            listOf(
                ToDoDetailState.UnInitialized,
                ToDoDetailState.Write
            )
        )
    }

    @Test
    fun `test Todo Insert`() = runBlockingTest {
        val detailTestObservable = detailViewModel.toDoDetailLiveData.test()
        val listTestObservable = listViewModel.todoListLiveData.test()

        detailViewModel.writeToDoItem(
            title = todo.title,
            description = todo.description
        )

        detailTestObservable.assertValueSequence(
            listOf(
                ToDoDetailState.UnInitialized,
                ToDoDetailState.Loading,
                ToDoDetailState.Success(todo)
            )
        )

        assert(detailViewModel.detailMode == DetailMode.DETAIL)
        assert(detailViewModel.id == id)

        listViewModel.fetchData()
        listTestObservable.assertValueSequence(
            listOf(
                ToDoListState.UnInitialized,
                ToDoListState.Loading,
                ToDoListState.Success(listOf(todo))
            )
        )
    }

}