package com.yonikim.aop_part5_chapter01.di

import com.yonikim.aop_part5_chapter01.data.repository.TestToDoRepository
import com.yonikim.aop_part5_chapter01.data.repository.ToDoRepository
import com.yonikim.aop_part5_chapter01.domain.todo.*
import com.yonikim.aop_part5_chapter01.presentation.detail.DetailMode
import com.yonikim.aop_part5_chapter01.presentation.detail.DetailViewModel
import com.yonikim.aop_part5_chapter01.presentation.list.ListViewModel
import org.koin.android.viewmodel.dsl.viewModel
import org.koin.dsl.module

internal val appTestModule = module {

    // ViewModel
    viewModel { ListViewModel(get(), get(), get()) }
    viewModel { (detailMode: DetailMode, id: Long) ->
        DetailViewModel(
            detailMode = detailMode,
            id = id,
            get(),
            get(),
            get(),
            get()
        )
    }

    // Use-Cases
    factory { GetToDoListUseCase(get()) }
    factory { InsertToDoItemUseCase(get()) }
    factory { InsertToDoListUseCase(get()) }
    factory { UpdateToDoItemUseCase(get()) }
    factory { GetToDoItemUseCase(get()) }
    factory { DeleteAllToDoItemUseCase(get()) }
    factory { DeleteToDoItemUseCase(get()) }

    // Repository
    single<ToDoRepository> { TestToDoRepository() }
}