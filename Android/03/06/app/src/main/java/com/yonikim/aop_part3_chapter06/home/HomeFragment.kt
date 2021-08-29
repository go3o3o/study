package com.yonikim.aop_part3_chapter06.home

import ChatListItem
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.View
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import com.google.android.material.snackbar.Snackbar
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.ktx.auth
import com.google.firebase.database.ChildEventListener
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.ktx.database
import com.google.firebase.ktx.Firebase
import com.yonikim.aop_part3_chapter06.DBKey.Companion.CHILD_CHAT
import com.yonikim.aop_part3_chapter06.DBKey.Companion.DB_ARTICLES
import com.yonikim.aop_part3_chapter06.DBKey.Companion.DB_USERS
import com.yonikim.aop_part3_chapter06.R
import com.yonikim.aop_part3_chapter06.databinding.FragmentHomeBinding

class HomeFragment : Fragment(R.layout.fragment_home) {

    private lateinit var articleAdapter: ArticleAdapter
    private lateinit var userDB: DatabaseReference
    private lateinit var articleDB: DatabaseReference

    private val articleList = mutableListOf<ArticleModel>()
    private val listener = object : ChildEventListener {
        override fun onChildAdded(snapshot: DataSnapshot, previousChildName: String?) {
            Log.d("HomeFragment", "onChildAdded")
            val articleModel = snapshot.getValue(ArticleModel::class.java)
            Log.d("HomeFragment", articleModel.toString())
            articleModel ?: return

            articleList.add(articleModel)
            articleAdapter.submitList(articleList)
        }

        override fun onChildChanged(snapshot: DataSnapshot, previousChildName: String?) {}
        override fun onChildRemoved(snapshot: DataSnapshot) {}
        override fun onChildMoved(snapshot: DataSnapshot, previousChildName: String?) {}
        override fun onCancelled(error: DatabaseError) {}

    }

    private var binding: FragmentHomeBinding? = null
    private val auth: FirebaseAuth by lazy {
        Firebase.auth
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val fragmentHomeBinding = FragmentHomeBinding.bind(view)
        binding = fragmentHomeBinding

        articleDB = Firebase.database.reference.child(DB_ARTICLES)
        userDB = Firebase.database.reference.child(DB_USERS)
        articleAdapter = ArticleAdapter(onItemClicked = { articleModel ->
            if (auth.currentUser != null) {
                if (auth.currentUser?.uid != articleModel.sellerId) {
                    val buyerId = auth.currentUser!!.uid
                    val sellerId = articleModel.sellerId
                    val itemTitle = articleModel.title
                    val chatRoomKey = "$buyerId#$sellerId#$itemTitle"
                    val chatRoom = ChatListItem(
                        buyerId = buyerId,
                        sellerId = sellerId,
                        itemTitle = itemTitle,
                        key = chatRoomKey
                    )
                    userDB.child(auth.currentUser!!.uid)
                        .child(CHILD_CHAT)
                        .push()
                        .setValue(chatRoom)
                    userDB.child(articleModel.sellerId)
                        .child(CHILD_CHAT)
                        .push()
                        .setValue(chatRoom)
                    Snackbar.make(view, "채팅방이 생성되었습니다. 채팅탭에서 확인해주세요.", Snackbar.LENGTH_LONG).show()

                } else {
                    Snackbar.make(view, "내가 올린 아이템입니다.", Snackbar.LENGTH_LONG).show()
                }
            } else {
                Snackbar.make(view, "로그인이 필요합니다.", Snackbar.LENGTH_LONG).show()
            }

        })

        Log.d("HomeFragment", "onViewCreated")

        fragmentHomeBinding.articleRecyclerView.layoutManager = LinearLayoutManager(context)
        fragmentHomeBinding.articleRecyclerView.adapter = articleAdapter

        fragmentHomeBinding.addArticleFloatingButton.setOnClickListener {
            context?.let {

                if (auth.currentUser != null) {
                    val intent = Intent(it, AddArticleActivity::class.java)
                    startActivity(intent)
                } else {
                    Snackbar.make(view, "로그인이 필요합니다.", Snackbar.LENGTH_LONG).show()
                }
            }
        }

        articleDB.addChildEventListener(listener)
    }

    override fun onResume() {
        super.onResume()

        Log.d("HomeFragment", "onResume")

        articleAdapter.notifyDataSetChanged()
    }

    override fun onDestroyView() {
        super.onDestroyView()

        Log.d("HomeFragment", "onDestroyView")
        articleDB.removeEventListener(listener)

    }


}