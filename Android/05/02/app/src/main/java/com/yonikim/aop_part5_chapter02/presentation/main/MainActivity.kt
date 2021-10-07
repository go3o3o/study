package com.yonikim.aop_part5_chapter02.presentation.main

import android.os.Bundle
import com.yonikim.aop_part5_chapter02.R
import com.yonikim.aop_part5_chapter02.databinding.ActivityMainBinding
import com.yonikim.aop_part5_chapter02.presentation.BaseActivity
import org.koin.android.ext.android.inject

internal class MainActivity : BaseActivity<MainViewModel, ActivityMainBinding>() {

    override val viewModel by inject<MainViewModel>()

    override fun getViewBinding(): ActivityMainBinding = ActivityMainBinding.inflate(layoutInflater)

    override fun observeData() {

    }
}