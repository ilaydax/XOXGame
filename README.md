# *XOXGame*
</br>
Bu proje Q-Learning algoritması ile geliştirilmiş bilgisayara karşı oynanan bir TicTacToe oyunudur.
</br>
</br>
Q-learning pekiştirmeli bir öğrenme algoritmasıdır. Algoritmadaki temel amaç, bir sonraki
hareketleri inceleyip yapacağı hareketlere göre kazanacağı ödülü görmek ve bu ödülü
çoklayıp (maxizimize) buna göre hareket etmektir. Yani her ödül (ceza), durum ve seçilen
eylemden en uygun eylemi öğrenmektir.
</br>
</br>
Q-learning algoritmasının çıktısı ise öğrenmenin kalitesini gösteren Q matrisidir. Q-learning
iteratif bir algoritmadır ve tüm değerleri başlangıçta 0 olan Q matrisi optimal değerlere
yakınsadığında sona erer. Algoritma her iterasyonda rastgele bir durumdan öğrenmeye
başlar, A (action)’ya göre durum değiştirir ve Q matrisini günceller. A’ya göre hedef duruma
ulaşıldığında iterasyon sona erer. A’ya göre bir durumdan birden fazla duruma geçis olabilir.
Böyle bir durumda, olası geçişlerden biri rastgele seçilir. Eğer seçilen durum hedef duruma
ulaştırmıyorsa, durum rastgele olacak durum olarak belirlenir. Hedef duruma ulaşılana kadar
iterasyon devam eder. Q matrisi aşağıdaki formüle göre güncellenir:
</br>

![image](https://github.com/ilaydax/TicTacToeGame/assets/93269919/b39652ce-60b3-4790-b1ee-4fae7138a270)

</br>

“Q(s,a)” (state, action) dediğimiz değer bizim şu anda {bulunduğumuz, gideceğimiz} dizin
</br>
“lr” dediğimiz değer öğrenme katsayısı (learning rate),
</br>
“r(s,a)” dediğimiz değer bizim {bulunduğumuz, gideceğimiz} ödül tablomuzdaki ödül değerimiz,
</br>
“Y” değeri gamma (discount rate),
</br>
“max(Q(s’,a’))” değeri ise gidebileceğimiz {gideceğimiz, gideceğimiz yerden gidebileceğimiz} yerlerin en yüksek Q değeridir.
</br>
Bizim projemizdeki Q-Learning algoritmasındaki değişkenleri değeri; lr = 0.1 Y = 0.9 
</br>
Gerçekleştirdiğimiz projede;
</br>

![image](https://github.com/ilaydax/TicTacToeGame/assets/93269919/aa71e3c0-662f-4c5b-898f-1cca8a340b7b)
</br>
 eğitim sürecinde modellerin kazanma verileri bu şekildedir.
</br>
Q Learning ile geliştirdiğimiz Tic Tac Toe oyununda;
</br>
“X” işaretini kullanan ve oyuna ilk başlayan oyuncu (Agent1) Q-learning yapısı ile eğittiğimiz bilgisayardır. “O” işaretini kullanan oyuncu (Agent2) ise bilgisayara karşı oynayan insandır.
</br>
Agent sınıfında model oluşturulmaktadır. TicTacToe sınıfında ise Agent sınıfında oluşturulan model eğitilmektedir.
</br>
Train fonksiyonu ile Agent1 ve Agent2 girilen rounds sayısı kadar oynamaktadırlar. 
</br>
Agent1 ve Agent2 eğitildikten sonra saveAgent() fonksiyonu ile Agent1 ile Agent2 modellerinin eğitim verileri kaydedilmektedir.
</br>
Daha sonra Agent1 yapay zekasının (bilgisayar) eğitim verileri yüklenmekte ve HumanPlayer fonksiyonu kullanılarak insana karşı oynamaktadır.
</br>
![image](https://github.com/ilaydax/TicTacToeGame/assets/93269919/2e13b4af-ef98-4f5b-864b-15b05f1338db)

![image](https://github.com/ilaydax/TicTacToeGame/assets/93269919/02de62ad-ce9e-4845-82a7-191b88f1184e)

![image](https://github.com/ilaydax/TicTacToeGame/assets/93269919/6a888eb7-ed0d-4d2c-a20e-e9ee2852c2df)









