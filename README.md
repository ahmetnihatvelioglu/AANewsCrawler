# DataMining

## Overwiev
This project is a web crawler that aims to automatically collect and save news from Anadolu Agency (AA) website. It pulls news from an ID range in the range, extracts the necessary information and supports JSON formats. It also downloads the visuals in the news and includes the related information.

## Key Features:

- **Automatic News Aggregation:** Automatically scans and pulls news within the specified ID range.

- **Data Extraction:** Extracts news headlines, summaries, content, dates, and categories.

- **JSON Data Record:** Saves the extracted news data to a file in JSON format.

- **Image Download:** Downloads images from news and saves them to a local folder.

- **Image Description Record:** Saves the descriptions of downloaded images to a separate CSV file.

- **Error Management:** Handles common web crawler errors such as connection problems and timeouts.

- **Flexible Configuration:** Parameters such as start and end IDs can be easily configured.


## Usage

- **main.py Dosyasını Çalıştırın:**

- main.py dosyasını çalıştırmak için aşağıdaki komutu kullanın:

  "python main.py"

- **Start Crawler:**

- main.py file starts pulling news using Crawler class in crawler.py file. Edit the relevant variables in main.py to set the ID range of news to pull:

  "crawler.get_news(start_id, end_id)"

- **Stopping Work:**

- While the crawler is running, you can stop the process at any time by pressing the Esc key.

- **Output Files:**

- The news pulled is saved in the news.json file.

- The downloaded images are saved in the ./images/ folder and a new subfolder is created for every 100 news items (for example, ./images/3313900/).

- The image descriptions are saved in the image_definitions.csv file.

## Project Structure

- The project consists of the following files and folders:

- **main.py:** Crawler'ı başlatan ana dosya.

- **crawler.py:** Temel crawler mantığını içeren sınıf tanımlamalarını barındırır.

- **data.py:** Haber nesnesini tanımlar.

- **news.json:** Çekilen haberlerin kaydedildiği JSON dosyası.

- **images/:** İndirilen görsellerin saklandığı klasör.

- **image_definitions.csv:** İndirilen görsellerin tanımlamalarının saklandığı CSV dosyası.












