let TheLanguage = "en";

function language() {
    if (TheLanguage === "en") {
        document.getElementById("WELCOME").innerText = "اهلا بك في V8 ZONE";

        document.getElementById("Paragraph").innerText = "اكتشف قوة السيارات وأسلوبها وإرثها من الأيقونات الكلاسيكية إلى الوحوش الحديثة - نقدم لك المواصفات التفصيلية والمراجعات وكل ما تحتاج إلى معرفته حول سياراتك المفضلة.";

        document.getElementById("Cars").innerText = "سيارات";
        document.getElementById("News").innerText = "الاخبار";
        document.getElementById("Sales").innerText = "المبيعات";
        document.getElementById("AboutUs").innerText = "من نحن";
        document.getElementById("ContactUs").innerText = "تواصل معنا";
        document.getElementById("LogOut").innerText = "تسجيل الخروج";
        document.getElementById("language").innerText = "اللغات";
        document.getElementById("Mazda").innerText = "مازدا";
        document.getElementById("Nissan").innerText = "نيسان";
        document.getElementById("Porsche").innerText = "بورش";
        document.getElementById("Tesla").innerText = "تسلا";
        document.getElementById("Chevorlet").innerText = "شيفروليه";
        document.getElementById("Mercedes").innerText = "مرسيدس";

        TheLanguage = "ar";
    } else if (TheLanguage === "ar") {
        document.getElementById("WELCOME").innerText = "WILLKOMMEN BEI V8 ZONE";

        document.getElementById("Paragraph").innerText = "Entdecken Sie die Kraft, den Stil und das Erbe der Autos – von klassischen Ikonen bis zu modernen Bestien. Wir bieten Ihnen detaillierte Spezifikationen, Bewertungen und alles, was Sie über Ihre Lieblingsautos wissen müssen.";

        document.getElementById("Cars").innerText = "Autos";
        document.getElementById("News").innerText = "Nachrichten";
        document.getElementById("Sales").innerText = "Verkäufe";
        document.getElementById("AboutUs").innerText = "Über uns";
        document.getElementById("ContactUs").innerText = "Kontakt";
        document.getElementById("LogOut").innerText = "Abmelden";
        document.getElementById("language").innerText = "Sprachen";
        document.getElementById("Mazda").innerText = "Mazda";
        document.getElementById("Nissan").innerText = "Nissan";
        document.getElementById("Porsche").innerText = "Porsche";
        document.getElementById("Tesla").innerText = "Tesla";
        document.getElementById("Chevorlet").innerText = "Chevrolet";
        document.getElementById("Mercedes").innerText = "Mercedes";

        TheLanguage = "de";
    } else {
        document.getElementById("WELCOME").innerText = "WELCOME TO V8 ZONE";

        document.getElementById("Paragraph").innerText = "Discover the Power, Style, and Legacy of Cars – From classic icons to modern beasts, we bring you detailed specs, reviews, and everything you need to know about your favorite cars.";

        document.getElementById("Cars").innerText = "Cars";
        document.getElementById("News").innerText = "News";
        document.getElementById("Sales").innerText = "Sales";
        document.getElementById("AboutUs").innerText = "About Us";
        document.getElementById("ContactUs").innerText = "Contact Us";
        document.getElementById("LogOut").innerText = "Log Out";
        document.getElementById("language").innerText = "Language";
        document.getElementById("Mazda").innerText = "Mazda";
        document.getElementById("Nissan").innerText = "Nissan";
        document.getElementById("Porsche").innerText = "Porsche";
        document.getElementById("Tesla").innerText = "Tesla";
        document.getElementById("Chevorlet").innerText = "Chevorlet";
        document.getElementById("Mercedes").innerText = "Mercedes";

        TheLanguage= "en";
    }
}
