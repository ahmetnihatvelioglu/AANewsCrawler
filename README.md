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

