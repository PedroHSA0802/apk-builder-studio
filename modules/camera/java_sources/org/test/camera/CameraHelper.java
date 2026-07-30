package org.test.camera;

import android.app.Activity;
import android.graphics.Color;
import android.view.ViewGroup;
import android.widget.FrameLayout;
import androidx.camera.core.CameraSelector;
import androidx.camera.core.ImageCapture;
import androidx.camera.core.ImageCaptureException;
import androidx.camera.core.Preview;
import androidx.camera.lifecycle.ProcessCameraProvider;
import androidx.camera.view.PreviewView;
import androidx.core.content.ContextCompat;
import androidx.lifecycle.LifecycleOwner;
import com.google.common.util.concurrent.ListenableFuture;
import java.io.File;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class CameraHelper {
    private Activity activity;
    private PreviewView previewView;
    private ImageCapture imageCapture;
    private ExecutorService cameraExecutor;

    public CameraHelper(Activity activity) {
        this.activity = activity;
        this.cameraExecutor = Executors.newSingleThreadExecutor();
    }

    public void startCamera() {
        // Muss im UI-Thread laufen, da wir UI-Elemente anfassen
        activity.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                setupCameraUI();
            }
        });
    }

    private void setupCameraUI() {
        // 1. Erstelle das View für die Vorschau
        previewView = new PreviewView(activity);
        
        // 2. Layout-Parameter: Wir machen es z.B. 500x500px groß oder Vollbild
        FrameLayout.LayoutParams params = new FrameLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, 
                ViewGroup.LayoutParams.MATCH_PARENT
        );
        
        // 3. Füge es der Activity hinzu (es liegt nun ÜBER Kivy)
        activity.addContentView(previewView, params);

        // 4. Kamera binden
        bindCameraUseCases();
    }

    private void bindCameraUseCases() {
        ListenableFuture<ProcessCameraProvider> cameraProviderFuture = 
            ProcessCameraProvider.getInstance(activity);

        cameraProviderFuture.addListener(() -> {
            try {
                ProcessCameraProvider cameraProvider = cameraProviderFuture.get();

                // Vorschau
                Preview preview = new Preview.Builder().build();
                preview.setSurfaceProvider(previewView.getSurfaceProvider());

                // Foto-Funktion
                imageCapture = new ImageCapture.Builder().build();

                // Rückkamera wählen
                CameraSelector cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA;

                // Alles entbinden und neu binden
                cameraProvider.unbindAll();
                
                // WICHTIG: Wir tun so, als wären wir LifecycleOwner (Kivy Activity ist es oft nicht direkt)
                // In einer echten App sollte man 'activity' casten, wenn sie AppCompatActivity ist.
                // Hier vereinfacht: Wir nutzen das Lifecycle der Activity, wenn möglich.
                cameraProvider.bindToLifecycle((LifecycleOwner) activity, cameraSelector, preview, imageCapture);

            } catch (Exception e) {
                e.printStackTrace();
            }
        }, ContextCompat.getMainExecutor(activity));
    }

    public void takePhoto(String filePath) {
        if (imageCapture == null) return;

        File photoFile = new File(filePath);
        ImageCapture.OutputFileOptions outputOptions = 
            new ImageCapture.OutputFileOptions.Builder(photoFile).build();

        imageCapture.takePicture(outputOptions, ContextCompat.getMainExecutor(activity), 
            new ImageCapture.OnImageSavedCallback() {
                @Override
                public void onImageSaved(ImageCapture.OutputFileResults outputFileResults) {
                    System.out.println("Foto gespeichert: " + filePath);
                }
                @Override
                public void onError(ImageCaptureException exception) {
                    exception.printStackTrace();
                }
            }
        );
    }
    
    public void closeCamera() {
         activity.runOnUiThread(() -> {
             if (previewView != null) {
                 ((ViewGroup) previewView.getParent()).removeView(previewView);
                 previewView = null;
             }
         });
    }
}
