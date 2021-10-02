package com.yonikim.lotto;

import android.content.Context;
import android.os.Handler;
import android.util.AttributeSet;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.widget.AppCompatTextView;

public class TypingWriter extends AppCompatTextView {
    private CharSequence myText;
    private int myIndex;
    private long myDelay = 150;

    public TypingWriter(@NonNull Context context) {
        super(context);
    }

    public TypingWriter(@NonNull Context context, @Nullable AttributeSet attrs) {
        super(context, attrs);
    }

    public TypingWriter(@NonNull Context context, @Nullable AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    private Handler myHandler = new Handler();
    private Runnable characterAddress = new Runnable() {
        @Override
        public void run() {
            setText(myText.subSequence(0, myIndex++));
            if (myIndex <= myText.length()) {
                myHandler.postDelayed(characterAddress, myDelay);
            }
        }
    };

    public void animateText(CharSequence text) {
        myText = text;
        myIndex = 0;
        setText("");
        myHandler.removeCallbacks(characterAddress);
        myHandler.postDelayed(characterAddress, myDelay);
    }

    public void setCharacterDelay(long millis) {
        myDelay = millis;
    }
}
