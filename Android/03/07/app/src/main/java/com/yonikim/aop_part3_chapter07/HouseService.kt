package com.yonikim.aop_part3_chapter07

import retrofit2.Call
import retrofit2.http.GET

interface HouseService {
    @GET("/v3/6ae5d5f8-127d-4655-bdb6-a37f2a798812")
    fun getHouseList(): Call<HouseDto>
}