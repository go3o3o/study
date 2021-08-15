package com.yonikim.aop_part3_chapter04.api

import com.yonikim.aop_part3_chapter04.Model.BestSellerDto
import com.yonikim.aop_part3_chapter04.Model.SearchBookDto
import retrofit2.http.GET
import retrofit2.http.Query
import retrofit2.Call

interface BookService {

    @GET("/api/search.api?output=json")
    fun getBookByName(
        @Query("key") apiKey: String,
        @Query("query") keyword: String
    ): Call<SearchBookDto>

    @GET("/api/bestSeller.api?output=json&categoryId=100")
    fun getBestSellerBooks(
        @Query("key") apiKey: String,
    ): Call<BestSellerDto>
}