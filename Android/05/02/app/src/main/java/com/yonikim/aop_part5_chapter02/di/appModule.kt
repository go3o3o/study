package com.yonikim.aop_part5_chapter02.di

import com.yonikim.aop_part5_chapter02.data.db.provideDB
import com.yonikim.aop_part5_chapter02.data.db.provideProductDao
import com.yonikim.aop_part5_chapter02.data.network.buildOkHttpClient
import com.yonikim.aop_part5_chapter02.data.network.provideGsonConverterFactory
import com.yonikim.aop_part5_chapter02.data.network.provideProductApiService
import com.yonikim.aop_part5_chapter02.data.network.provideProductRetrofit
import com.yonikim.aop_part5_chapter02.data.repository.DefaultProductRepository
import com.yonikim.aop_part5_chapter02.data.repository.ProductRepository
import com.yonikim.aop_part5_chapter02.domain.GetProductItemUseCase
import com.yonikim.aop_part5_chapter02.presentation.detail.ProductDetailViewModel
import com.yonikim.aop_part5_chapter02.domain.GetProductListUseCase
import com.yonikim.aop_part5_chapter02.domain.OrderProductItemUseCase
import com.yonikim.aop_part5_chapter02.presentation.list.ProductListViewModel
import com.yonikim.aop_part5_chapter02.presentation.main.MainViewModel
import com.yonikim.aop_part5_chapter02.presentation.profile.ProfileViewModel
import kotlinx.coroutines.Dispatchers
import org.koin.android.ext.koin.androidApplication
import org.koin.android.viewmodel.dsl.viewModel
import org.koin.dsl.module

val appModule = module {

    // ViewModel
    viewModel { MainViewModel() }
    viewModel { ProductListViewModel(get()) }
    viewModel { ProfileViewModel() }
    viewModel { (productId: Long) -> ProductDetailViewModel(productId, get(), get()) }

    // Coroutines Dispatcher
    single { Dispatchers.Main }
    single { Dispatchers.IO }

    // Use-Cases
    factory { GetProductItemUseCase(get()) }
    factory { GetProductListUseCase(get()) }
    factory { OrderProductItemUseCase(get()) }

    // Repositories
    single<ProductRepository> { DefaultProductRepository(get(), get(), get()) }

    single { provideGsonConverterFactory() }

    single { buildOkHttpClient() }

    single { provideProductRetrofit(get(), get()) }

    single { provideProductApiService(get()) }

    // Database
    single { provideDB(androidApplication()) }
    single { provideProductDao(get()) }

}