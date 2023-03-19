# AutonomousDrivingAssistant
Araç asistanı, sizinle sözlü iletişim kurabilen, diyaloğunuzu anlayabilen ve araç için hedefler belirleyebilen özelliklere sahiptir.
![People (1)](https://user-images.githubusercontent.com/87595266/226173442-ccfb2b4a-7c36-44e5-9443-59911ba8064b.png)

# Proje Hakkında

Bu, türkçe doğal dil modeli kullanılarak oluşturulmuş bir otonom sürüş asistanı projesidir. Proje, Google Speech To Text hizmetini konuşmanızı tanımak, Google Text To Speech hizmetini sizinle sözlü iletişim kurmak için kullanır. Konuşmalarınız, tasarladığımız doğal dil modeli tarafından işlenir ve anlaşılır hale getirilir, bu sayede otonom araç asistanı nereye gitmek istediğinizi anlayabilir.

Proje uygulaması için ROS2 sistemini ve Webots Tesla simülasyon ortamını kullanıyoruz. Ayrıca, otonom araçların dar bir paralel park alanından çıkmasını sağlamak için geliştirdiğimiz KNN modelini de bu projede kullanıyoruz.

Proje ayrıntıları ve demo videosu için Youtube videosunu izleyebilirsiniz.

# Youtube Proje Tanıtımı & Demo

https://youtu.be/kXKoH2fnbSc

# Proje Ortamı Nasıl Oluşturulur?

Projeyi çalıştırmak için ROS2 Humble ve webots_ros2 paketlerine, ayrıca Webots simülasyon ortamına ihtiyacınız olacaktır. 
Aşağıdaki talimatları takip edin. Bu talimatlar ROS2 Humble ve Webots simülasyon ortamını kurduğunuzu varsayar.

- Bir `ros2_ws` klasörü oluşturun ve içine `src` klasörü oluşturun. Daha sonra, aşağıdaki bağlantıdaki `Install webots_ros2 from sources` bölümündeki talimatları izleyin.

    [Install webots_ros2 from sources](https://github.com/cyberbotics/webots_ros2/wiki/Linux-Installation-Guide#install-webots_ros2-from-sources)
   
- `tesla_voice_control` paketini `ros2_ws/src/webots_ros2/` dizinine taşıyın. Bu paket, simülasyon ortamını başlatmanızı sağlar.

- Sonrasında, `voice_control` paketini `ros2_ws/src/` dizinine taşıyın. Bu, otonom sürüş asistanınızı başlatmak için gereklidir.

## Başlangıç

1. Çalışma dizininizde, `ros2_ws` dizini içinde `colcon build` kullanarak proje derleyin.
2. Robotu başlatmak için bir terminalde `ros2 launch tesla_voice_control robot_launch.py` komutunu çalıştırın. Bu komut simulasyon ortamını başlatacaktır.
3. Başka bir terminalde `ros2 run voice_control voice_control` komutunu çalıştırarak sürüş asistanını başlatın.
4. Demo'yu test etmek için yüksek sesle "Eve gitmek istiyorum" deyin. Otonom araç park yerinden çıkacak ve evinize doğru hareket etmeye başlayacaktır. Ev hedefine ulaştığında sürüş asistanınız geri bildirim vererek aracı durduracaktır.

* `data.csv` dosyası Türk doğal dil modeli kullanmak için oluşturulmuş veri kümesini içermektedir.
