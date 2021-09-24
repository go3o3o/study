package com.yonikim.aop_part4_chapter05

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.core.view.isGone
import com.yonikim.aop_part4_chapter05.databinding.ActivitySearchBinding
import com.yonikim.aop_part4_chapter05.view.RepositoryRecyclerAdapter
import kotlinx.coroutines.*
import kotlin.coroutines.CoroutineContext

class SearchActivity : AppCompatActivity(), CoroutineScope {

    private val job = Job()
    override val coroutineContext: CoroutineContext
        get() = Dispatchers.Main + job

    private lateinit var binding: ActivitySearchBinding
    private lateinit var adapter: RepositoryRecyclerAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySearchBinding.inflate(layoutInflater)
        setContentView(binding.root)

        initAdapter()
        initViews()
        bindViews()

    }

    private fun initAdapter() = with(binding) {
        adapter = RepositoryRecyclerAdapter()
    }

    private fun initViews() = with(binding) {
        emptyResultView.isGone = true
        recyclerView.adapter = adapter
    }

    private fun bindViews() = with(binding) {
    searchButton.setOnClickListener {

    }
    }
    private fun searchKeyword(keyword: String) = launch {
        withContext(Dispatchers.IO) {

        }
    }
}