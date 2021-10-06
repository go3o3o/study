package com.yonikim.aop_part5_chapter02.di

import com.yonikim.aop_part5_chapter02.data.network.buildOkHttpClient
import com.yonikim.aop_part5_chapter02.data.network.provideGsonConverterFactory
import com.yonikim.aop_part5_chapter02.data.network.provideProductApiService
import com.yonikim.aop_part5_chapter02.data.network.provideProductRetrofit
import org.koin.dsl.module

val appModule = module {

    single { provideGsonConverterFactory() }

    single { buildOkHttpClient() }

    single { provideProductRetrofit(get(), get()) }

    single { provideProductApiService(get()) }

}