# Tryhackme Capture Room

### Türkçe:

Bugün Tryhackme'de bulunan bir capture odasının çözümünü ele alacağız. Bu odada, iki farklı wordlist içinde kullanıcı adları ve şifreler yer almaktadır. Öncelikle, brute force saldırısı yapmadan önce başka bir çözüm yolunun olup olmadığını araştırdım. Ancak, açık bir port, servis veya dizin bulamadım. Son olarak, SQL enjeksiyonu denedikten sonra brute force yöntemine karar verdim.

Brute force saldırısı yaparken, belirli bir deneme sayısından sonra captcha doğrulaması isteniyordu. Ancak, captcha bize karışık bir metin veya görsel olarak değil, direk HTML sayfasının içindeki bir matematik işlemi olarak sunuluyordu. Bu nedenle, Python ile web scraping yaparak matematik sorusunu otomatik olarak çözecek ve brute force saldırısına devam edecek bir kod yazdım.

Programın çalışma mantığı şu şekildedir: İlk olarak, program sırayla kullanıcı adlarını dener ve "The user {username} does not exist" ifadesini görmediği zaman kullanıcı adını bulur. Daha sonra, bulduğu kullanıcı adını aynı mantıkla dener ve "Invalid password for user '{username}'" ifadesini görmediği zaman şifreyi bulur.


Not: Python kodunda url kısmını hedef makinenize göre tekrardan düzenleyiniz. <br>
Not 2: Programın bulunduğu dizine capture odasının size verdiği usernames.txt ve passwords.txt dosyalarını aynı dizine atınız.




### English:

Today we will discuss the solution to a capture room on TryHackMe. In this room, there are two wordlists containing usernames and passwords. Initially, I tried to find a solution other than a brute force attack, but I could not find any open port, service, or directory. Finally, I decided to use brute force after trying SQL injection.

During the brute force attack, after a certain number of attempts, a captcha verification was required. However, the captcha was not presented as a scrambled text or image, but rather as a math problem embedded in the HTML page. Therefore, I wrote a Python code to scrape the web and automatically solve the math problem, and then continue the brute force attack.

The program works as follows: First, the program tries usernames one by one and finds the username when it does not see the message "The user {username} does not exist". Then, using the same logic, it tries the found username and finds the password when it does not see the message "Invalid password for user '{username}'".

Note: Please adjust the URL in the Python code according to your target machine. <br>
Note 2: Please place the usernames.txt and passwords.txt files provided by the capture room in the same directory as the program.
