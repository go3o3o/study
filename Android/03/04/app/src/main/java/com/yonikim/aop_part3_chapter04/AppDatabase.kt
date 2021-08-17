package com.yonikim.aop_part3_chapter04

import androidx.room.Database
import androidx.room.RoomDatabase
import com.yonikim.aop_part3_chapter04.Model.History
import com.yonikim.aop_part3_chapter04.dao.HistoryDao

@Database(entities = [History::class], version = 1)
abstract class AppDatabase: RoomDatabase() {
    abstract fun historyDao(): HistoryDao
}