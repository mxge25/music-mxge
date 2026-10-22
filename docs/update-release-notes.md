# MXGE Player build 7 + MXGE Links 0.3.0

Not yet verified on physical devices. The cutter is experimental.

Experimental companion. Downloads from supported public links are not yet verified on physical devices.

تحديث الواجهة: الثيم الكحلي والموف المعتمد، أيقونات أصلية دائرية، وإعدادات في خمس مجموعات. قائمة الثلاث شرط داخل المشغّل تضم السرعة والإبطاء والصوت، القص، تعديل بيانات الأغنية، التشغيل من البداية، سجل المواضع، مؤقت النوم، تكرار A–B، الكلمات والفصول والعلامات. تبقى حالة المؤقت/التكرار الفعالة ظاهرة في المشغّل. تعديل البيانات محلي داخل MXGE ولا يغيّر وسوم الملف الأصلي.

MXGE Links 0.3.0: ابدأ بملف **universal.apk** الذي يضم ARM64 وARMv7 (99,951,146 bytes؛ أقل من 100 MB). نسخ أصغر متاحة بمعمارية محددة. لم يُحسم سبب رسالة App not installed على الهاتف؛ النسخة الشاملة تزيل اختيار المعمارية الخاطئة كسبب محتمل، ولا تُعتبر إثباتًا لنجاح التثبيت على كل جهاز. انتظر اكتمال تنزيل APK وافتحه من التنزيلات مع مساحة كافية لفك المحرك. ملف المصدر ZIP للمطورين.

Android 8+; Player base version code 7 (ARM64 2007 / ARMv7 1007), companion version code 3. Same application IDs and release certificate: install as updates while retaining local data. Player remains entirely offline with no INTERNET permission. Only the independent companion uses internet.

Companion supports selecting M4A audio or compatible MP4/H.264 video up to 720p from supported public YouTube, Instagram, TikTok and Facebook links. Keep its screen visible during downloading. Private, login-only, protected or changed services may fail. Current prebuilt runtime supports 4 KiB memory-page devices only; 16 KiB devices are rejected before native startup.

Validation: clean Flutter analysis; the existing suite was run, then all seven affected layout scenarios passed after fixes, with the other 54 tests already passing. Arabic/English, 360dp portrait, landscape and 2× text were checked with widget fixtures. Signed APK identities, Android permissions, notification icon resources and ZIP alignment verified. Companion APK payloads remain byte-for-byte unchanged through lossless recompression; no runtime shrinking. Each of the five signed APKs is strictly below 100,000,000 bytes. No connected physical phone was available: installation, platform downloads, audio/Bluetooth, notifications, cutter accuracy/memory and performance still require device tests.

The companion-only GPL application-source ZIP includes its original Kotlin/UI/build source, lockfile, Gradle wrapper, packaging scripts, license notices and upstream source directions. Player source stays PRIVATE and is excluded. Exact producing-build provenance for the pinned third-party prebuilt native runtime remains unresolved upstream; the archive is not claimed to reconstruct every native producing build. See its SOURCES.md before broader redistribution.

Compare downloads against SHA256SUMS.txt. Older releases are retained.
