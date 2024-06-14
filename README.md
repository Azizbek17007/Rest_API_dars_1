# Rest_API_dars_1

REST API (Representational State Transfer Application Programming Interface) — bu veb-servislarni yaratish va ulardan foydalanish uchun ishlatiladigan arxitektura tamoyillari va qoidalar to'plamidir. REST API veb-ilovalarga boshqa dasturlar bilan muloqot qilish imkonini beradi, bu esa turli tizimlar va platformalar o'rtasida o'zaro aloqalarni osonlashtiradi.

REST API'ning asosiy tamoyillari:

1. **Resurslar**: REST API'da barcha narsa resurs sifatida ko'rib chiqiladi. Resurslar URL orqali manzillanadi. Masalan, `https://example.com/users` URL manzili "users" resursini ifodalaydi.

2. **HTTP usullari**: REST API HTTP protokolidan foydalanadi va asosiy usullar quyidagilar:
    - **GET**: Resursni olish uchun.
    - **POST**: Yangi resurs yaratish uchun.
    - **PUT**: Mavjud resursni yangilash uchun.
    - **DELETE**: Resursni o'chirish uchun.

3. **Stateless**: Har bir so'rov (request) mustaqil bo'lishi kerak, ya'ni server mijozning oldingi so'rovlarini eslab qolmasligi kerak. Barcha kerakli ma'lumotlar so'rov ichida bo'lishi kerak.

4. **Client-Server arxitekturasi**: Klient (mijoz) va server o'rtasida aniq ajratish mavjud bo'lib, mijoz serverdan faqat kerakli resurslarni so'raydi va oladi. Mijoz va server mustaqil rivojlanishi mumkin.

5. **Cacheable**: Resurslarni keshlash (cache) mumkin. Bu serverning yuklamasini kamaytirish va javob berish vaqtini tezlashtirish uchun muhim.

6. **Layered System**: Tizim qatlamli bo'lishi mumkin, ya'ni mijoz oddiygina interfeys orqali resursga murojaat qiladi, lekin resursning asl manbasi bir necha qatlam orqasida yashiringan bo'lishi mumkin.

REST API'larni yaratishda va foydalanishda JSON va XML kabi ma'lumot almashish formatlari keng qo'llaniladi. JSON (JavaScript Object Notation) formati yengil va inson o'qishi oson bo'lgani uchun ko'pincha afzal ko'riladi.

REST API'dan foydalanish misoli:

- **GET so'rovi**: `GET https://example.com/users/1` bu so'rov 1-id raqamli foydalanuvchi haqidagi ma'lumotlarni oladi.
- **POST so'rovi**: `POST https://example.com/users` bu so'rov yangi foydalanuvchi yaratish uchun ishlatiladi, va so'rov tanasida foydalanuvchi ma'lumotlari JSON formatida yuboriladi.

REST API zamonaviy veb-ilovalar va xizmatlar orasida juda mashhur va keng tarqalgan, chunki u oddiy va moslashuvchan muloqot imkoniyatlarini taqdim etadi.
