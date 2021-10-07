package com.yonikim.aop_part5_chapter02.di

import com.yonikim.aop_part5_chapter02.data.network.buildOkHttpClient
import com.yonikim.aop_part5_chapter02.data.network.provideGsonConverterFactory
import com.yonikim.aop_part5_chapter02.data.network.provideProductApiService
import com.yonikim.aop_part5_chapter02.data.network.provideProductRetrofit
import com.yonikim.aop_part5_chapter02.data.repository.DefaultProductRepository
import com.yonikim.aop_part5_chapter02.data.repository.ProductRepository
import com.yonikim.aop_part5_chapter02.domain.GetProductItemUseCase
import kotlinx.coroutines.Dispatchers
import org.koin.dsl.module

val appModule = module {

    // Coroutines Dispatcher
    single { Dispatchers.Main }
    single { Dispatchers.IO }

    // Use-Cases
    factory { GetProductItemUseCase(get()) }

    // Repositories
    single<ProductRepository> { DefaultProductRepository(get(), get()) }

    single { provideGsonConverterFactory() }

    single { buildOkHttpClient() }

    single { provideProductRetrofit(get(), get()) }

    single { provideProductApiService(get()) }

}