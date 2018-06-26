report_link = [
    {
        "topic": {"th": "อุปทาน", "en": "supply"},
        "sub_topic": [
            # {
            #     "th": "รายได้เกษตรกร",
            #     "en": "farm-income"
            # },
            # {
            #     "th": "ดัชนีผลผลิตภาคอุตสาหกรรม",
            #     "en": "manufacturing-production-index"
            # },
            # {
            #     "th": "เครื่องชี้ประกอบของภาคอุตสาหกรรม",
            #     "en": "other-manufacturing-indicators"
            # },
            # {
            #     "th": "อัตราการใช้กำลังการผลิตที่ขจัดฤดูกาล",
            #     "en": "capacity-utilization"
            # },
            # {
            #     "th": "เครื่องชี้ภาคบริการ",
            #     "en": "service-serctor-indicators"
            # },
        ]
    }, {
        "topic": {"th": "อุปสงค์ในประเทศ", "en": "demand"},
        "sub_topic": [
            {
                "th": "การบริโภคภาคเอกชน",
                "en": "private-consumption-indicators",
                "type": "normal",
                "url": "http://www2.bot.or.th/statistics/Download/EC_EI_003_S2_ENG_ALL.CSV"
            },
            #### { "th": "การใช้จ่ายในหมวดสินค้าคงทนและกึ่งคงทน", "en": "durable-index-and-semi-durable-index" },
            #### { "th": "การใช้จ่ายในหมวดสินค้าไม่คงทน", "en": "nielsen-fmcg-index" },
            #### { "th": "การใช้จ่ายในหมวดบริการ", "en": "service-index-and-net-tourist-spending-index" },

            {
                "th": "ความเชื่อมั่นผู้บริโภค",
                "en": "consumer-confidence-index",
                "type": "normal",
                "url": "http://www2.bot.or.th/statistics/Download/EC_EI_034_ENG_ALL.CSV"
            },
            {
                "th": "การลงทุนภาคเอกชน",
                "en": "private-investment-indicators",
                "type": "normal",
                "url": "http://www2.bot.or.th/statistics/Download/EC_EI_004_S2_ENG_ALL.CSV"
            },
            #--- { "th": "การลงทุนด้านเครื่องจักรและอุปกรณ์", "en": "equipment-indicators" },
            #--- { "th": "การลงทุนด้านก่อสร้าง", "en": "construction-indicators" },
            {
                "th": "ความเชื่อมั่นธุรกิจ",
                "en": "business-sentiment-index",
                "type": "normal",
                "url": "http://www2.bot.or.th/statistics/Download/EC_EI_005_ENG_ALL.CSV"
            },
            #--- { "th": "รายจ่ายของรัฐบาล", "en": "central-government-expenditure" },
            #--- { "th": "รายได้องรัฐบาลและดุลการคลัง", "en": "fiscal-position-and-government-revenue" },
        ]
    }, {
        "topic": {"th": "ภาคต่างประเทศ", "en": "external-sector"},
        "sub_topic": [
            # {
            #     "th": "ภาวะเศรษฐกิจประเทศอุตสาหกรรมหลัก (G3)",
            #     "en": "g3-manufacturing-pmi"
            # },
            # {
            #     "th": "มูลค่าการส่งออกของประเทศในกลุ่มเอเชีย",
            #     "en": "asian-export-performance",
            # },
            {
                "th": "มูลค่าการส่งออกสินค้าของไทย",
                "en": "export-growth",
                "type": "normal",
                "url": "http://www2.bot.or.th/statistics/Download/EC_XT_001_ENG_ALL.CSV"
            },
            #### { "th": "มูลค่าการนำเข้าสินค้าของไทย", "en": "import-growth" },

            #--- { "th": "ดุลบัญชีการเคลื่อนย้าย", "en": "financial-account" }, 
            #--- { "th": "ดุลบัญชีเดินสะพัดและดุลการชำระเงิน", "en": "balance-of-payments" },
            #--- { "th": "จำนวนนักท่องเที่ยวต่างชาติ", "en": "inbound-tourists-by-country" },
        ]
    }, {
        "topic": {"th": "ภาวะการเงิน", "en": "monerary-condition"},
        "sub_topic": [
            {
                "th": "อัตราดอกเบี้ยของธนาคารพาณิชย์",
                "en": "commericial-bank-interest",
                "type": "normal",
                "url": "http://www2.bot.or.th/statistics/Download/FM_RT_002_ENG_ALL.CSV"
            },
            #### { "th": "ต้นทุนการระดมทุนผ่านตราสารหนี้", "en": "government-bond-yield" },

            # {
            #     "th": "ปริมาณการระดมทุนภาคธุรกิจ",
            #     "en": "change-in-total-corporate-financing"
            # },
            # {
            #     "th": "ปริมาณสินเชื่อใหม่ของ ODCs ที่ให้แก่เอกชน",
            #     "en": "new-private-credit-extended"
            # },
            {
                "th": "อัตราการแลกเปลี่ยน",
                "en": "exchange-rates",
                "type": "normal",
                "url": "http://www2.bot.or.th/statistics/Download/EC_EI_007_ENG_ALL.CSV"
            },
            #--- { "th": "ความผันผวนของค่าเงินบาทเทียบกับภูมิภาค", "en": "regional-exchange-rate-volatility" },
        ]
    }, {
        "topic": {"th": "เสถียรภาพเศรษฐกิจการเงิน", "en": "finanacial-stability"},
        "sub_topic": [
            {
                "th": "อัตราเงินเฟ้อทั่วไป",
                "en": "contribution-to-headline-inflation",
                "type": "normal",
                "url": "http://www2.bot.or.th/statistics/Download/EC_EI_027_ENG_ALL.CSV"
            },
            #### { "th": "อัตราเงินเฟ้อพื้นฐาน", "en": "contribution-to-core-inflation" },

            {
                "th": "อัตราการว่างงาน และการจ้างงาน",
                "en": "unemployment-and-employment-rate",
                "type": "normal",
                "url": "http://www2.bot.or.th/statistics/Download/EC_RL_009_S4_ENG_ALL.CSV"
            },
            #--- { "th": "ประมาณการหนี้ต่างประเทศ", "en": "external-debt-outstanding" },
            #--- { "th": "เสถียรภาพด้านต่างประเทศของไทย", "en": "external-stability-indicator" },
        ]
    },
]
