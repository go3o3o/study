package com.yonikim.lotto

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.airbnb.lottie.LottieAnimationView
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.AdView
import com.yonikim.lotto.databinding.ActivityDesireBinding
import com.yonikim.lotto.databinding.ActivityMainBinding

class DesireActivity: AppCompatActivity() {

    private lateinit var binding: ActivityDesireBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityDesireBinding.inflate(layoutInflater)
        setContentView(binding.root)

        initMobileAds()

        // TODO DesireButton 클릭시 playAnimating -> MainActivity
        initViews()
    }

    private fun initViews() = with(binding) {
        desireButton.setOnClickListener {
            desireButton.playAnimation()
            launchMainActivity()
        }
    }

    private fun launchMainActivity() {
        startActivity(Intent(this, MainActivity::class.java).apply {
            addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK)
            addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        })
    }

    private fun initMobileAds() {
        val adView = findViewById<AdView>(R.id.adView)
        val adRequest = AdRequest.Builder().build()
        adView.loadAd(adRequest);
    }

}