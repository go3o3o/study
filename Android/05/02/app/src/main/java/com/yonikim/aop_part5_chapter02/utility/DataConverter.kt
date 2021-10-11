package com.yonikim.aop_part5_chapter02.utility

import androidx.room.TypeConverter
import java.util.*

object DataConverter {

    @TypeConverter
    fun toDate(dateLong: Long?): Date? {
        return if (dateLong == null) null else Date(dateLong)
    }

    @TypeConverter
    fun fromDate(date: Date?): Long? {
        return date?.time
    }
}