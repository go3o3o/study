package com.yonikim.aop_part4_chapter05

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Toast
import androidx.core.view.isGone
import com.yonikim.aop_part4_chapter05.data.entity.GithubRepoEntity
import com.yonikim.aop_part4_chapter05.databinding.ActivitySearchBinding
import com.yonikim.aop_part4_chapter05.utility.RetrofitUtil
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
            searchKeyword(searchBarInputView.text.toString())
        }
    }

    private fun searchKeyword(keyword: String) = launch {
        withContext(Dispatchers.IO) {
            val response = RetrofitUtil.githubApiService.searchRepositories(keyword)
            if (response.isSuccessful) {
                val body = response.body()
                withContext(Dispatchers.Main) {
                    body?.let {
                        setData(it.items)
                    }
                }
            }
        }
    }

    private fun setData(items: List<GithubRepoEntity>) {
        adapter.setSearchResultList(items) {
            Toast.makeText(this, "이름: ${it.toString()}", Toast.LENGTH_SHORT).show()
            startActivity(
                Intent(this, RepositoryActivity::class.java).apply {
                    putExtra(RepositoryActivity.REPOSITORY_OWNER_KEY, it.owner.login)
                    putExtra(RepositoryActivity.REPOSITORY_NAME_KEY, it.name)
                }
            )
        }
    }
}