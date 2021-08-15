package com.yonikim.aop_part3_chapter04

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import com.yonikim.aop_part3_chapter04.Model.BestSellerDto
import com.yonikim.aop_part3_chapter04.api.BookService
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val retrofit = Retrofit.Builder()
            .baseUrl("https://book.interpark.com")
            .addConverterFactory(GsonConverterFactory.create())
            .build()

        val bookService = retrofit.create(BookService::class.java)
        bookService.getBestSellerBooks(API_KEY)
            .enqueue(object : Callback<BestSellerDto> {
                override fun onResponse(
                    call: Call<BestSellerDto>,
                    response: Response<BestSellerDto>
                ) {
                    if (response.isSuccessful.not()) {
                        return
                    }
                    response.body()?.let {
                        Log.d(TAG, it.toString())
                        it.books.forEach { book ->
                            Log.d(TAG, book.toString())

                        }

                    }

                }

                override fun onFailure(call: Call<BestSellerDto>, t: Throwable) {

                }
            })
    }

    companion object {
        private const val API_KEY =
            "EB9D1F31B2F7131171B01AB2B7CE6D91B12B1F45717C970717E83F0FE388EF65"
        private const val TAG = "MainActivity"
    }
}