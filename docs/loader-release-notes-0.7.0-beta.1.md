# MXGE Loader 0.7.0-beta.1 · build 8

هوية جديدة بالكامل: كحلي وبنفسجي كهربائي ولايم، لوجو split-wing أصلي وأيقونات متناسقة. بحث ولصق وتنزيل ومكتبة أبسط، مع جودات واضحة وحالات تنزيل ملوّنة. أضيف تنزيل صور منشورات إنستجرام وفيسبوك العامة عندما يتيح المصدر بياناتها، وحفظها في Pictures/MXGE Loader. الفيديو والصوت يظلان في Movies/Music. تحديث مباشر فوق النسخة القديمة؛ لا تحذف التطبيق.

- Reduced repeated progress-card rebuilding, cached fonts/previews and shared thumbnail requests. Hardware speed/frame-rate gains have not been measured.
- Public-post photos retain JPEG/PNG/WebP bytes, use fresh source URLs and verify MIME, dimensions and transfer length. Video covers/social previews are excluded. Restricted/login-only responses can fail.
- Lossless APK compression retains every uncompressed payload, ABI, codec, feature and font. Universal **99.89 MB**, ARM64 **56.40 MB**, ARMv7 **49.76 MB**. Same package/signature; Player and prior releases preserved.
- Native build/lint and signed-package gates passed. Existing native unit-test task is NO-SOURCE. Twelve focused temporary host parser checks passed; they are not Android/platform service tests. No new project test suite.

**Experimental companion. Downloads from supported public links are not yet verified on physical devices.**

No device/AVD is available: native UI, source-photo downloads, Gallery/OEM indexing, cross-app sharing and background behavior need phone validation. Video/audio runtime targets Android 8+ ARM devices with 4KB pages; 16KB pages remain unsupported by that native runtime. Photo downloads also depend on source availability. No login/cookie collection, advertising, account or backend. Player remains offline and private.

Choose Universal for one APK supporting both ARM architectures, or an ABI APK for a smaller download. Verify SHA256SUMS.txt. Source ZIP contains Loader only, its integration/build tools and existing licenses; no Player source or signing material. Native producing-build provenance limits remain in SOURCES.md. Existing releases are retained.
