package com.yonikim.aop_part5_chapter04.adapter

import android.net.Uri
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.yonikim.aop_part5_chapter04.databinding.ViewholderPhotoItemBinding
import com.yonikim.aop_part5_chapter04.extensions.loadCenterCrop

class PhotoListAdapter(
    private val removePhotoListener: (Uri) -> Unit
) : RecyclerView.Adapter<PhotoListAdapter.ProductItemViewHolder>() {

    private var imageUriList: List<Uri> = listOf()

    inner class ProductItemViewHolder(
        private val binding: ViewholderPhotoItemBinding
    ) : RecyclerView.ViewHolder(binding.root) {
        fun bindData(data: Uri) = with(binding) {
            photoImageView.loadCenterCrop(data.toString(), 8f)
        }

        fun bindViews(data: Uri) = with(binding) {
            closeButton.setOnClickListener {
                removePhotoListener(data)
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ProductItemViewHolder {
        val view =
            ViewholderPhotoItemBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return ProductItemViewHolder(view)
    }

    override fun onBindViewHolder(holder: ProductItemViewHolder, position: Int) {
        val imageUri = imageUriList[position]
        holder.bindData(imageUri)
        holder.bindViews(imageUri)
    }

    override fun getItemCount(): Int = imageUriList.size

    fun setPhotoList(imageUriList: List<Uri>) {
        this.imageUriList = imageUriList
        notifyDataSetChanged()
    }
}