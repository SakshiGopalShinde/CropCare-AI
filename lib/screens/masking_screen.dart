import 'dart:io';
import 'dart:typed_data';
import 'package:file_picker/file_picker.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

class MaskingScreen extends StatefulWidget {
  const MaskingScreen({super.key});

  @override
  State<MaskingScreen> createState() => _MaskingScreenState();
}

class _MaskingScreenState extends State<MaskingScreen> {
  Uint8List? webImageBytes;
  Uint8List? webMaskBytes;

  File? selectedImage;
  File? maskImage;

  final String basePath = r"D:\sih_last\CropCareAI-main\NWRD\train";

  Future<void> pickImage() async {
    final res = await FilePicker.platform.pickFiles(
      allowMultiple: false,
      allowedExtensions: ['png', 'jpg', 'jpeg'],
      type: FileType.custom,
      initialDirectory: "$basePath\\images",
      withData: kIsWeb, // Required for web
    );

    if (res == null) return;

    final picked = res.files.single;

    if (kIsWeb) {
      // --- Web Mode ---
      webImageBytes = picked.bytes;

      String fileName = picked.name;
      String folder = "$basePath\\masks\\$fileName";

      // ❗ Web cannot read File() from your PC => we simulate mask by blank or disable mask
      webMaskBytes = null;

      setState(() {});
      return;
    }

    // --- Desktop / Android Mode ---
    selectedImage = File(picked.path!);

    findMask();
  }

  void findMask() {
    if (selectedImage == null) return;

    String fileName = selectedImage!.path.split("\\").last;
    String maskPath = "$basePath\\masks\\$fileName";

    File f = File(maskPath);

    setState(() {
      maskImage = f.existsSync() ? f : null;
    });

    if (!f.existsSync()) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("⚠ Mask not found for: $fileName")),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Early Disease Masking View"),
        backgroundColor: Colors.green,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            ElevatedButton.icon(
              onPressed: pickImage,
              icon: const Icon(Icons.folder_open),
              label: const Text("Select Image"),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.green.shade600,
                padding: const EdgeInsets.all(16),
              ),
            ),

            const SizedBox(height: 20),

            Expanded(
              child: Center(
                child: kIsWeb
                    ? _buildWebViewer()
                    : _buildDesktopViewer(),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildDesktopViewer() {
    if (selectedImage == null) {
      return const Text("No image selected", style: TextStyle(fontSize: 18));
    }

    return Row(
      children: [
        Expanded(
          child: Column(
            children: [
              const Text("Original Image", style: TextStyle(fontSize: 18)),
              const SizedBox(height: 10),
              Expanded(child: Image.file(selectedImage!, fit: BoxFit.contain))
            ],
          ),
        ),
        const SizedBox(width: 20),
        Expanded(
          child: Column(
            children: [
              const Text("Mask Image", style: TextStyle(fontSize: 18)),
              const SizedBox(height: 10),
              Expanded(
                child: maskImage != null
                    ? Image.file(maskImage!, fit: BoxFit.contain)
                    : const Text("❌ No Mask Found"),
              )
            ],
          ),
        ),
      ],
    );
  }

  Widget _buildWebViewer() {
    if (webImageBytes == null) {
      return const Text("Upload image to preview", style: TextStyle(fontSize: 18));
    }

    return Column(
      children: [
        const Text("Web Preview: Mask not available on Web Sandbox"),
        const SizedBox(height: 10),
        Expanded(child: Image.memory(webImageBytes!, fit: BoxFit.contain)),
      ],
    );
  }
}
