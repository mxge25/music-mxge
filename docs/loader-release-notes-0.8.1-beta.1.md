# MXGE Loader 0.8.1-beta.1 · code 12

إصلاح مسار تنزيل يوتيوب كصوت: اختيار مسار الصوت المتاح وقت التنزيل، وفصل التنزيل عن التحويل المحلي. حالات واضحة لتجهيز المحرك والاتصال والتنزيل والتحويل والفحص والحفظ، مع نسبة تحويل محسوبة من تقدم FFmpeg الفعلي.

M4A ينسخ صوت AAC الموجود بدون إعادة ضغط، وMP3 يتحول إلى 192kbps. الإيقاف يوقف محوّل الصوت مباشرة، والمصدر المكتمل يفضل محفوظًا لإعادة المحاولة بدون تنزيله مرة أخرى. لو العملية توقفت بدون تقدم دقيقتين، تنتهي برسالة واضحة بدل الانتظار المفتوح. الأجزاء المحفوظة والإصدارات القديمة محفوظة. الملفات النهائية تُفحص قبل الحفظ الافتراضي في **Music/MXGE Loader**.

Desktop checks: three public YouTube samples, including a 634.62-second video, produced M4A and MP3 files that fully decoded and contained audio only. Compressed AAC packets in M4A matched the source. The compiled converter was exercised with host Android adapters for progress, cancellation and retry; a deliberately stalled child was stopped after about 120 seconds with its source retained. Kotlin compilation/lint and package checks passed. No new app dependency or permission. Player build 10 is unchanged.

**Experimental companion. Downloads from supported public links are not yet verified on physical devices.**

The user's exact phone hang was not reproduced: no link/device log or connected phone was available, and the previous desktop path also passed the short samples. This release addresses verified weaknesses in progress, child-process cancellation, stale YouTube selectors and unbounded transfer waits. Source restrictions, 4KiB ARM runtime limits and unverified Android MediaStore/background/upgrade behavior remain. Install over the existing Loader without uninstalling. If an old task is still running, pause it once and resume after updating.
