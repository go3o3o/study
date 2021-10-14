package com.yonikim.aop_part5_chapter02.presentation.profile

import android.app.Activity
import android.util.Log
import androidx.activity.result.contract.ActivityResultContracts
import androidx.core.view.isGone
import androidx.core.view.isVisible
import com.google.android.gms.auth.api.signin.GoogleSignIn
import com.google.android.gms.auth.api.signin.GoogleSignInOptions
import com.google.android.gms.common.api.ApiException
import com.google.firebase.auth.FirebaseAuth
import com.yonikim.aop_part5_chapter02.R
import com.yonikim.aop_part5_chapter02.databinding.FragmentProfileBinding
import com.yonikim.aop_part5_chapter02.presentation.BaseFragment
import org.koin.android.ext.android.inject

internal class ProfileFragment : BaseFragment<ProfileViewModel, FragmentProfileBinding>() {

    companion object {
        const val TAG = "ProfileFragment"
    }

    override val viewModel by inject<ProfileViewModel>()

    override fun getViewBinding(): FragmentProfileBinding =
        FragmentProfileBinding.inflate(layoutInflater)

    private val gso: GoogleSignInOptions by lazy {
        GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
            .requestIdToken(getString(R.string.default_web_client_id))
            .requestEmail()
            .build()
    }

    private val gsc by lazy {
        GoogleSignIn.getClient(requireActivity(), gso)
    }
    private val firebaseAuth by lazy { FirebaseAuth.getInstance() }

    private val loginLauncher =
        registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
            if (result.resultCode == Activity.RESULT_OK) {
                val task = GoogleSignIn.getSignedInAccountFromIntent(result.data)
                try {
                    task.getResult(ApiException::class.java)?.let { account ->
                        Log.d(TAG, "firebaseAuthWithGoogle $account")
                    } ?: throw Exception()
                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }
        }

    override fun observeData() = viewModel.profileStateLiveData.observe(this) {
        when (it) {
            is ProfileState.UnInitialized -> initViews()
            is ProfileState.Loading -> handleLoadingState()
            is ProfileState.Login -> TODO()
            is ProfileState.Success -> handleSuccessState(it)
            is ProfileState.Error -> TODO()
        }

    }

    private fun initViews() = with(binding) {
        loginButton.setOnClickListener {
            signInGoogle()
        }
        logoutButton.setOnClickListener {

        }
    }

    private fun signInGoogle() {
        val signInIntent = gsc.signInIntent
        loginLauncher.launch(signInIntent)

    }

    private fun handleLoadingState() = with(binding) {
        progressBar.isVisible = true
        loginRequiredGroup.isGone = true
    }

    private fun handleSuccessState(state: ProfileState.Success) = with(binding) {
        progressBar.isGone = true
        when(state) {
            is ProfileState.Success.Registered -> {
                handleRegisteredState()
            }
            is ProfileState.Success.NotRegistered -> {
                profileGroup.isGone = true
                loginRequiredGroup.isVisible = true
//                adapter.setProductList(listOf())
            }
        }
    }

    private fun handleRegisteredState() {

    }


}