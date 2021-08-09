package com.yonikim.aop_part3_chapter03

import android.app.TimePickerDialog
import android.content.Context
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import java.util.*

class MainActivity : AppCompatActivity() {

    private val onOffButton: Button by lazy {
        findViewById(R.id.onOffButton)
    }
    private val changeAlarmTimeButton: Button by lazy {
        findViewById(R.id.changeAlarmTimeButton)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // TODO
        // Step0. 뷰 초기화
        initOnOffButton()
        initChangeAlarmTimeButton()
        // Step1. 데이터 가져오기
        // Step2. 뷰에 데이터 그려주기
    }

    private fun initOnOffButton() {
        onOffButton.setOnClickListener {

        }
    }

    private fun initChangeAlarmTimeButton() {
        changeAlarmTimeButton.setOnClickListener {
            val calendar = Calendar.getInstance()
            TimePickerDialog(this, { picker, hour, minute ->
                val model = saveAlarmModel(hour, minute, onOff = false)

            }, calendar.get(Calendar.HOUR_OF_DAY), calendar.get(Calendar.MINUTE), false).show()
        }
    }

    private fun saveAlarmModel(hour: Int, minute: Int, onOff: Boolean): AlarmDisplayModel {
        val model = AlarmDisplayModel(hour = hour, minute = minute, onOff = onOff)

        val sharedPreferences = getSharedPreferences("time", Context.MODE_PRIVATE)
        with(sharedPreferences.edit()) {
            putString("alarm", model.makeDataForDB())
            putBoolean("onOff", model.onOff)
            commit()
        }
        return model
    }
}