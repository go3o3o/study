package com.yonikim.lotto.koLotto

import android.os.Bundle
import android.os.CountDownTimer
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.AdView
import com.yonikim.lotto.R
import com.yonikim.lotto.databinding.ActivityKoLotto645Binding
import com.yonikim.lotto.databinding.ActivityMainBinding

class KoLotto645Activity : AppCompatActivity() {
    private lateinit var binding: ActivityKoLotto645Binding
    //    private val clearButton: Button by lazy {
//        findViewById<Button>(R.id.clearButton)
//    }
//    private val autoSelectButton: Button by lazy {
//        findViewById<Button>(R.id.autoSelectButton)
//    }
//    private val saveButton: Button by lazy {
//        findViewById<Button>(R.id.saveButton)
//    }

    private val numberTextViewList: List<TextView> by lazy {
        listOf<TextView>(
            findViewById<TextView>(R.id.lottoNumber1),
            findViewById<TextView>(R.id.lottoNumber2),
            findViewById<TextView>(R.id.lottoNumber3),
            findViewById<TextView>(R.id.lottoNumber4),
            findViewById<TextView>(R.id.lottoNumber5),
            findViewById<TextView>(R.id.lottoNumber6)
        )
    }


    private var isRun = false
    private val pickNumberSet = hashSetOf<Int>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityKoLotto645Binding.inflate(layoutInflater)
        setContentView(binding.root)

//        numberPicker.minValue = 1
//        numberPicker.maxValue = 45

//        initRunButton()
//        initAddButton()
//        initClearButton()
        initMobileAds()
    }

    private fun initMobileAds() = with(binding) {
        val adRequest = AdRequest.Builder().build()
        adView.loadAd(adRequest)
    }

//    private fun initRunButton() {
//        runButton.setOnClickListener {
//            val list = getRandomNumber()
//
//            isRun = true
//
//            list.forEachIndexed { index, number ->
//                val textView = numberTextViewList[index]
//
//                textView.text = number.toString()
//                textView.isVisible = true
//
//                setNumberBackground(number, textView)
//            }
//
//            isRun = true
//        }
//    }

    private fun getRandomNumber(): List<Int> = with(binding) {
        val numberList = mutableListOf<Int>()
            .apply {
                for (i in 1..45) {
                    if (pickNumberSet.contains(i)) {
                        continue
                    }
                    this.add(i)
                }
            }
        numberList.shuffle()

        val newList = pickNumberSet.toList() + numberList.subList(0, 6 - pickNumberSet.size)
        return newList.sorted()
    }

    private fun setNumberBackground(number: Int, textView: TextView) = with(binding) {
        when (number) {
            in 1..10 -> textView.background =
                ContextCompat.getDrawable(this, R.drawable.circle_yello)
            in 11..20 -> textView.background =
                ContextCompat.getDrawable(this, R.drawable.circle_blue)
            in 21..30 -> textView.background =
                ContextCompat.getDrawable(this, R.drawable.circle_red)
            in 31..40 -> textView.background =
                ContextCompat.getDrawable(this, R.drawable.circle_grey)
            else -> textView.background = ContextCompat.getDrawable(this, R.drawable.circle_green)
        }
    }

    val countDownTimer = object : CountDownTimer(3000, 100) {
        override fun onTick(millisUntilFinished: Long) {
            numberTextViewList.forEach {
                val randomNumber = (Math.random() * 45 + 1).toInt()
                it.text = "$randomNumber"
            }
        }

        override fun onFinish() {
        }

    }

//    private fun initAddButton() {
//        addButton.setOnClickListener {
//            if (isRun) {
//                Toast.makeText(this, "초기화 후에 시도하세요.", Toast.LENGTH_SHORT).show()
//                return@setOnClickListener
//            }
//            if (pickNumberSet.size >= 5) {
//                Toast.makeText(this, "번호는 5개까지만 선택할 수 있습니다.", Toast.LENGTH_SHORT).show()
//                return@setOnClickListener
//            }
////            if (pickNumberSet.contains(numberPicker.value)) {
////                Toast.makeText(this, "이미 선택한 번호입니다.", Toast.LENGTH_SHORT).show()
////                return@setOnClickListener
////            }
//            val textView = numberTextViewList[pickNumberSet.size]
//            textView.isVisible = true
////            textView.text = numberPicker.value.toString()
//
////            setNumberBackground(numberPicker.value, textView)
//
////            pickNumberSet.add(numberPicker.value)
//        }
//    }

//    private fun initClearButton() {
//        clearButton.setOnClickListener {
//            pickNumberSet.clear()
//            numberTextViewList.forEach {
//                it.isVisible = false
//            }
//            isRun = false
//        }
//    }
}