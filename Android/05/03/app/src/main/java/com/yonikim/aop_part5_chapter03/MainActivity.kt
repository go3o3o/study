package com.yonikim.aop_part5_chapter03

import android.Manifest
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.hardware.display.DisplayManager
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.camera.core.AspectRatio
import androidx.camera.core.CameraSelector
import androidx.camera.core.ImageCapture
import androidx.camera.core.ImageCapture.CAPTURE_MODE_MINIMIZE_LATENCY
import androidx.camera.core.ImageCapture.FLASH_MODE_AUTO
import androidx.camera.core.Preview
import androidx.camera.lifecycle.ProcessCameraProvider
import androidx.camera.view.PreviewView
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import com.yonikim.aop_part5_chapter03.databinding.ActivityMainBinding
import java.util.concurrent.ExecutorService
import java.util.concurrent.Executors

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var cameraExecutor: ExecutorService
    private lateinit var imageCapture: ImageCapture

    private val cameraProviderFuture by lazy { ProcessCameraProvider.getInstance(this) }
    private val displayManager by lazy {
        getSystemService(Context.DISPLAY_SERVICE) as DisplayManager
    }
    private var displayId: Int = -1

    private val displayListener = object : DisplayManager.DisplayListener {
        override fun onDisplayAdded(displayId: Int) {}

        override fun onDisplayRemoved(displayId: Int) {}

        override fun onDisplayChanged(displayId: Int) {
            if (this@MainActivity.displayId == displayId) {

            }
        }

    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        if (allPermissionsGranted()) {
            startCamera(binding.viewFinder)
        } else {
            ActivityCompat.requestPermissions(
                this, REQUIRED_PERMISSIONS, REQUEST_CODE_PERMISSIONS
            )
        }
    }

    private fun allPermissionsGranted() = REQUIRED_PERMISSIONS.all {
        ContextCompat.checkSelfPermission(
            baseContext, it
        ) == PackageManager.PERMISSION_GRANTED
    }

    private fun startCamera(viewFinder: PreviewView) {
        displayManager.registerDisplayListener(displayListener, null)
        cameraExecutor = Executors.newSingleThreadExecutor()
        viewFinder.postDelayed({
            displayId = viewFinder.display.displayId
            bindCameraUseCase()
        }, 10)
    }

    private fun bindCameraUseCase() = with(binding) {
        val rotation = viewFinder.display.rotation
        val cameraSelector = CameraSelector.Builder().requireLensFacing(LENS_FACING).build()

        cameraProviderFuture.addListener({
            val cameraProvider: ProcessCameraProvider = cameraProviderFuture.get()
            val preview = Preview.Builder().apply {
                setTargetAspectRatio(AspectRatio.RATIO_4_3)
                setTargetRotation(rotation)
            }
            val imageCaptureBuilder = ImageCapture.Builder()
                .setCaptureMode(CAPTURE_MODE_MINIMIZE_LATENCY)
                .setTargetAspectRatio(AspectRatio.RATIO_4_3)
                .setTargetRotation(rotation)
                .setFlashMode(FLASH_MODE_AUTO)
            imageCapture = imageCaptureBuilder.build()

            try {
                cameraProvider.unbindAll() // 기존에 바인딩 되어 있는 카메라는 해제를 해준다.
                
            } catch (e: Exception) {

            }
        })
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == REQUEST_CODE_PERMISSIONS) {
            if (allPermissionsGranted()) {
                startCamera(binding.viewFinder)
            } else {
                Toast.makeText(this, "카메라 권한이 없습니다.", Toast.LENGTH_SHORT).show()
                finish()
            }
        }
    }

    companion object {
        private const val REQUEST_CODE_PERMISSIONS = 10
        private val REQUIRED_PERMISSIONS = arrayOf(Manifest.permission.CAMERA)
        private val LENS_FACING: Int = CameraSelector.LENS_FACING_BACK
    }

}