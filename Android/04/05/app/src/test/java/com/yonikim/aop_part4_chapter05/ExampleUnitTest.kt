package com.yonikim.aop_part4_chapter05

import kotlinx.coroutines.async
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import org.junit.Test

import org.junit.Assert.*
import kotlin.system.measureTimeMillis

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * See [testing documentation](http://d.android.com/tools/testing).
 */
class ExampleUnitTest {
    @Test
    fun addition_isCorrect() {
        assertEquals(4, 2 + 2)
    }

    @Test
    fun test01() = runBlocking {
        val time = measureTimeMillis {
            val firstName = getFirstName()
            val lastName = getLastName()
            print("Hello, $lastName $firstName")
        }
        print("$time")
    }

    @Test
    fun test02() = runBlocking {
        val time = measureTimeMillis {
            val firstName = async { getFirstName() }
            val lastName = async { getLastName()}
            print("Hello, ${lastName.await()} ${firstName.await()}")
        }
        print("$time")
    }

    suspend fun getFirstName(): String {
        delay(1000)
        return "요니"
    }
    suspend fun getLastName(): String {
        delay(1000)
        return "킴"
    }
}