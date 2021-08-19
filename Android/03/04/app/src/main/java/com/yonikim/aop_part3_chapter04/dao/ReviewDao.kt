package com.yonikim.aop_part3_chapter04.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import com.yonikim.aop_part3_chapter04.Model.Review

@Dao
interface ReviewDao {
    @Query("SELECT * FROM review WHERE id = :id")
    fun getReview(id: Int): Review

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    fun saveReview(review: Review)
}