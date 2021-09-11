package com.yonikim.aop_part4_chapter02.service

import retrofit2.Call
import retrofit2.http.GET

interface MusicService {

    @GET("/v3/d1ca2d9e-f8a8-47fb-b1d6-99d40ef1feaf")
    fun listMusics(): Call<MusicDto>
}