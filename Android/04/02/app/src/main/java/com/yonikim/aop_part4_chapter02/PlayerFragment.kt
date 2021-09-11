package com.yonikim.aop_part4_chapter02

import android.os.Bundle
import android.util.Log
import android.view.View
import androidx.core.view.isVisible
import androidx.fragment.app.Fragment
import com.yonikim.aop_part4_chapter02.databinding.FragmentPlayerBinding
import com.yonikim.aop_part4_chapter02.service.MusicDto
import com.yonikim.aop_part4_chapter02.service.MusicService
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class PlayerFragment : Fragment(R.layout.fragment_player) {
    private var binding: FragmentPlayerBinding? = null
    private var isWatchingPlayListView = true

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val fragmentPlayerBinding = FragmentPlayerBinding.bind(view)

        initPlayListButton(fragmentPlayerBinding)

        getVideoListFromServer()
    }

    private fun initPlayListButton(fragmentPlayerBinding: FragmentPlayerBinding) {
        fragmentPlayerBinding.playListImageView.setOnClickListener {
            // TODO 데이터 로딩이 완료되지 않은 경우
            fragmentPlayerBinding.playerViewGroup.isVisible = isWatchingPlayListView
            fragmentPlayerBinding.playListViewGroup.isVisible = isWatchingPlayListView.not()

            isWatchingPlayListView = !isWatchingPlayListView
        }
    }

    private fun getVideoListFromServer() {
        val retrofit = Retrofit.Builder()
            .baseUrl("https://run.mocky.io")
            .addConverterFactory(GsonConverterFactory.create())
            .build()

        retrofit.create(MusicService::class.java)
            .also {
                it.listMusics()
                    .enqueue(object : Callback<MusicDto> {
                        override fun onResponse(
                            call: Call<MusicDto>,
                            response: Response<MusicDto>
                        ) {
                            response.body()?.let {
                                val modelList = it.musics.mapIndexed { index, musicEntity ->
                                    musicEntity.mapper(index.toLong())
                                }
                            }
                        }

                        override fun onFailure(call: Call<MusicDto>, t: Throwable) {
                        }

                    })
            }
    }

    companion object {
        fun newInstance(): PlayerFragment {
            return PlayerFragment()
        }
    }
}