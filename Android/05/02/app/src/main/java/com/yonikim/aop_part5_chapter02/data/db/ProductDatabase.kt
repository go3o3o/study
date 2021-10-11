package com.yonikim.aop_part5_chapter02.data.db

import androidx.room.Database
import androidx.room.RoomDatabase
import androidx.room.TypeConverters
import com.yonikim.aop_part5_chapter02.data.db.dao.ProductDao
import com.yonikim.aop_part5_chapter02.data.entity.product.ProductEntity
import com.yonikim.aop_part5_chapter02.utility.DataConverter

@Database(
    entities = [ProductEntity::class],
    version = 1,
    exportSchema = false
)

@TypeConverters(DataConverter::class)
abstract class ProductDatabase: RoomDatabase() {
    companion object {
        const val DB_NAME = "ProductDatabase.db"
    }

    abstract fun productDao(): ProductDao
}