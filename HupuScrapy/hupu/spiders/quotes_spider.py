import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = ['https://voice.hupu.com/nba/2470690.html']
        for line in open("hu.txt", 'r'):
            line = 'https://voice.hupu.com/nba/' + line.strip() + '.html'
            print(line)
            urls.append(line.strip())
        print(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
            title = response.xpath('/html/body/div[4]/div[1]/div[1]/h1/text()').extract()[0].strip()
            author = response.xpath('//*[@id="source_baidu"]/a/text()'
                                 ).extract()[0].strip()
            time = response.xpath('//*[@id="pubtime_baidu"]/text()').extract()[0].strip()

       #     print(title, '\n', author, '\n', time)
        #    page = response.url.split("/")[-1].split(".")[0]
       #     filename = '%s.txt' % page
       #     f = open(filename, "w+", encoding='utf-8')
       #     f.write(title)
       #     f.write('\n')
       #     f.write(author)
        #    f.write('\n')
       #     f.write(time)
       #     f.write('\n')

            content = ''
            for k in response.xpath('/html/body/div[4]/div[1]/div[2]/div/div[2]/p/text()').extract():
                content = content + k
            yield {
                'title': title,
                'name': author,
                'time': time,
                'content': content
            }
        except IOError:
            print("Error: 没有找到文件或读取文件失败")
        else:
            print("内容写入文件成功")

#   '//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/h1/text()'
#     with open(filename, 'w') as f:
#            f.write(title, '\n', author)

