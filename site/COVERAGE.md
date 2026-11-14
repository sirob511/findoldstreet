# FindOldStreet coverage report

As of 14 November 2026. Initial, incomplete source-backed release. A verified row establishes a documented rename, not a verified present-day map identity.

9,675 published records across 33 countries: 9,573 streets/segments, 79 cities and 23 country-name mappings.

The [source audit](data/source-audit.json) inventories all repository source manifests, including failures and uncited leads. It is not an exhaustive worldwide source census.

| Country | Published streets / segments | Rename events | Localities | Review |
|---|---:|---:|---:|---:|
| Ukraine | 5111 | 5111 | 206 | 28 |
| Poland | 962 | 1043 | 4 | 0 |
| South Africa | 81 | 81 | 4 | 9 |
| Vietnam | 3 | 3 | 1 | 2 |
| Kazakhstan | 346 | 346 | 3 | 1 |
| India | 8 | 8 | 2 | 2 |
| Uzbekistan | 656 | 656 | 1 | 0 |
| Lithuania | 1173 | 1173 | 1 | 0 |
| Czechia | 510 | 510 | 1 | 0 |
| Moldova | 622 | 622 | 1 | 0 |
| Estonia | 101 | 101 | 1 | 0 |

## Expansion passes

| Pass | Target | New published | Total published | Scope |
|---|---:|---:|---:|---|
| 1 | 500 | 837 | 2482 | Dnipro postal street-name mappings |
| 2 | 500 | 759 | 3241 | Kharkiv postal street-name mappings |
| 3 | 500 | 788 | 4029 | Odesa and Zaporizhzhia postal street-name mappings |
| 4 | 500 | 1049 | 5078 | Vinnytsia, Poltava, Chernihiv and Cherkasy postal street-name mappings |
| 5 | 500 | 786 | 5864 | Mykolaiv, Zhytomyr, Rivne and Sumy street mappings, plus 13 city renames |
| 6 | 500 | 656 | 6520 | Tashkent, Uzbekistan: explicit directory street pairs, conflicts and unresolved chains excluded |
| 7 | 500 | 749 | 7269 | Wrocław, Poland: historical German names with exact current municipal name/type matches |
| 8 | 500 | 1173 | 8442 | Vilnius, Lithuania: pre-1987 and historical names checked against captured current road-name inventory |
| 9 | 500 | 510 | 8952 | Brno, Czechia: museum-backed street histories, current-index checks and abolished-street exclusions |
| 10 | 500 | 723 | 9675 | Chișinău, Moldova and Tallinn, Estonia: municipal-library name tables and EKI documented renames |

Pass 9: Final review withheld 59 combined, alternate-name-list or isolated-house labels from the original commit. Displayed totals count retained records.

## City and country renamings

Initial selection; the street counts above exclude these records.

- Dnipropetrovsk → Dnipro (city); [source](https://www.rada.gov.ua/en/news/News/top_news/131134.html).
- Dniprodzerzhynsk → Kamianske (city); [source](https://www.rada.gov.ua/en/news/News/top_news/131134.html).
- Swaziland → Eswatini (country); [source](https://digitallibrary.un.org/record/1282124).
- Орджонікідзе → Покров (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Артемове → Залізне (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Артемівськ → Бахмут (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Дзержинськ → Торецьк (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Димитров → Мирноград (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Кіровське → Хрестівка (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Комсомольське → Кальміуське (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Красний Лиман → Лиман (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Торез → Чистякове (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Юнокомунарівськ → Бунге (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Красноармійськ → Покровськ (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Кіровоград → Кропивницький (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Ульяновка → Благовіщенське (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Кіровськ → Голубівка (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Красний Луч → Хрустальний (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Вахрушеве → Боково-Хрустальне (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Петровське → Петрово-Красносілля (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Краснодон → Сорокине (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Артемівськ → Кипуче (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Свердловськ → Довжанськ (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Стаханов → Кадіївка (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Червонопартизанськ → Вознесенівка (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Іллічівськ → Чорноморськ (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Котовськ → Подільськ (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Комсомольськ → Горішні Плавні (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Червонозаводське → Заводське (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Кузнецовськ → Вараш (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Цюрупинськ → Олешки (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Щорс → Сновськ (city); [source](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf).
- Bangalore → Bengaluru (city); [source](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/387496/Karnataka_State_India_Name_Changes_20141112.pdf).
- Mangalore → Mangaluru (city); [source](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/387496/Karnataka_State_India_Name_Changes_20141112.pdf).
- Bellary → Ballari (city); [source](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/387496/Karnataka_State_India_Name_Changes_20141112.pdf).
- Bijapur → Vijayapura (city); [source](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/387496/Karnataka_State_India_Name_Changes_20141112.pdf).
- Belgaum → Belagavi (city); [source](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/387496/Karnataka_State_India_Name_Changes_20141112.pdf).
- Chikmagalur → Chikkamagaluru (city); [source](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/387496/Karnataka_State_India_Name_Changes_20141112.pdf).
- Gulbarga → Kalaburagi (city); [source](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/387496/Karnataka_State_India_Name_Changes_20141112.pdf).
- Mysore → Mysuru (city); [source](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/387496/Karnataka_State_India_Name_Changes_20141112.pdf).
- Hospet → Hosapete (city); [source](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/387496/Karnataka_State_India_Name_Changes_20141112.pdf).
- Shimoga → Shivamogga (city); [source](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/387496/Karnataka_State_India_Name_Changes_20141112.pdf).
- Hubli → Hubballi (city); [source](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/387496/Karnataka_State_India_Name_Changes_20141112.pdf).
- Tumkur → Tumakuru (city); [source](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/387496/Karnataka_State_India_Name_Changes_20141112.pdf).
- Madras → Chennai (city); [source](https://assets.publishing.service.gov.uk/media/6ab67e78997a4b2950ccef41/India_Toponymic_Factfile.pdf).
- Calcutta → Kolkata (city); [source](https://assets.publishing.service.gov.uk/media/6ab67e78997a4b2950ccef41/India_Toponymic_Factfile.pdf).
- Trivandrum → Thiruvananthapuram (city); [source](https://assets.publishing.service.gov.uk/media/6ab67e78997a4b2950ccef41/India_Toponymic_Factfile.pdf).
- Port Blair → Sri Vijaya Puram (city); [source](https://assets.publishing.service.gov.uk/media/6ab67e78997a4b2950ccef41/India_Toponymic_Factfile.pdf).
- Sài Gòn → Hồ Chí Minh City (city); [source](https://assets.publishing.service.gov.uk/media/6a3a740deaee00074150f25f/Vietnam_Toponymic_Factfile.pdf).
- Нур-Султан → Астана (city); [source](https://www.akorda.kz/ru/o-pereimenovanii-goroda-nur-sultana-stolicy-respubliki-kazahstan-v-gorod-astanu-stolicu-respubliki-kazahstan-1782457).
- Warmbaths → Bela-Bela (city); [source](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf).
- Port Elizabeth → Gqeberha (city); [source](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf).
- Uitenhage → Kariega (city); [source](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf).
- East London → KuGompo City (city); [source](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf).
- Messina → Musina (city); [source](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf).
- Katkop → Ngqayi (city); [source](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf).
- Maclear → Nqanqarhu (city); [source](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf).
- Pietersburg → Polokwane (city); [source](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf).
- King William’s Town → Qonce (city); [source](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf).
- Graaff-Reinet → Robert Sobukwe (city); [source](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf).
- Kudube → Thema (city); [source](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf).
- Driehoek → Uhelo (city); [source](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf).
- Brandfort → Winnie Mandela (city); [source](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf).
- Aberdeen → Xamdeboo (city); [source](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf).
- Makhado → Louis Trichardt (city); [source](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf).
- Ceylon → Sri Lanka (country); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- Dahomey → Benin (country); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- Upper Volta → Burkina Faso (country); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- Zaire → Democratic Republic of the Congo (country); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- Western Samoa → Samoa (country); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- Siam → Thailand (country); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- Persia → Iran (country); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- Transjordan → Jordan (country); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- Surinam → Suriname (country); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- Rumania → Romania (country); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- Burma → Myanmar (country); [source](https://unstats.un.org/unsd/methodology/m49/).
- Cape Verde → Cabo Verde (country); [source](https://unstats.un.org/unsd/methodology/m49/).
- Ivory Coast → Côte d’Ivoire (country); [source](https://unstats.un.org/unsd/methodology/m49/).
- Turkey → Türkiye (country); [source](https://unstats.un.org/unsd/methodology/m49/).
- East Timor → Timor-Leste (country); [source](https://unstats.un.org/unsd/methodology/m49/).
- Democratic Kampuchea → Cambodia (country); [source](https://unstats.un.org/unsd/methodology/m49/).
- Czech Republic → Czechia (country); [source](https://unstats.un.org/unsd/methodology/m49/).
- Macedonia → North Macedonia (country); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- Basutoland → Lesotho (country); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- Nyasaland → Malawi (country); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- British Honduras → Belize (country); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- New Hebrides → Vanuatu (country); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- Léopoldville → Kinshasa (city); [source](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present).
- Allahabad → Prayagraj (city); [source](https://prayagrajdivision.nic.in/about-department/introduction/).
- Новомосковськ → Самар (city); [source](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80).
- Першотравенськ → Шахтарське (city); [source](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%A8%D0%B0%D1%85%D1%82%D0%B0%D1%80%D1%81%D1%8C%D0%BA%D0%B5).
- Первомайськ → Сокологірськ (city); [source](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%A1%D0%BE%D0%BA%D0%BE%D0%BB%D0%BE%D0%B3%D1%96%D1%80%D1%81%D1%8C%D0%BA).
- Молодогвардійськ → Отаманівка (city); [source](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%9E%D1%82%D0%B0%D0%BC%D0%B0%D0%BD%D1%96%D0%B2%D0%BA%D0%B0).
- Сєвєродонецьк → Сіверськодонецьк (city); [source](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%A1%D1%96%D0%B2%D0%B5%D1%80%D1%81%D1%8C%D0%BA%D0%BE%D0%B4%D0%BE%D0%BD%D0%B5%D1%86%D1%8C%D0%BA).
- Червоноград → Шептицький (city); [source](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%A8%D0%B5%D0%BF%D1%82%D0%B8%D1%86%D1%8C%D0%BA%D0%B8%D0%B9).
- Дружба → Хутір-Михайлівський (city); [source](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%A5%D1%83%D1%82%D1%96%D1%80-%D0%9C%D0%B8%D1%85%D0%B0%D0%B9%D0%BB%D1%96%D0%B2%D1%81%D1%8C%D0%BA%D0%B8%D0%B9).
- Красноград → Берестин (city); [source](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%91%D0%B5%D1%80%D0%B5%D1%81%D1%82%D0%B8%D0%BD).
- Первомайський → Златопіль (city); [source](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%97%D0%BB%D0%B0%D1%82%D0%BE%D0%BF%D1%96%D0%BB%D1%8C).
- Ватутіне → Багачеве (city); [source](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%91%D0%B0%D0%B3%D0%B0%D1%87%D0%B5%D0%B2%D0%B5).
- Підгородне → Підгороднє (city); [source](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%9F%D1%96%D0%B4%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BD%D1%94).
- Южне → Південне (city); [source](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%9F%D1%96%D0%B2%D0%B4%D0%B5%D0%BD%D0%BD%D0%B5).
- Южноукраїнськ → Південноукраїнськ (city); [source](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%9F%D1%96%D0%B2%D0%B4%D0%B5%D0%BD%D0%BD%D0%BE%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA).

## Locality coverage

| Country | Locality (source spelling) | Published | Events | Review |
|---|---|---:|---:|---:|
| Ukraine | Івано-Франкове | 2 | 2 | 0 |
| Ukraine | Андріянів | 1 | 1 | 0 |
| Ukraine | Бабина | 1 | 1 | 0 |
| Ukraine | Баня Лисовицька | 1 | 1 | 0 |
| Ukraine | Бартатів | 2 | 2 | 0 |
| Ukraine | Батиїв | 1 | 1 | 0 |
| Ukraine | Бендюга | 1 | 1 | 0 |
| Ukraine | Береги | 2 | 2 | 0 |
| Ukraine | Берездівці | 1 | 1 | 0 |
| Ukraine | Блищиводи | 1 | 1 | 0 |
| Ukraine | Борислав | 4 | 4 | 0 |
| Ukraine | Борок | 1 | 1 | 0 |
| Ukraine | Бортники | 1 | 1 | 0 |
| Ukraine | Боршів | 1 | 1 | 0 |
| Ukraine | Борятин | 1 | 1 | 0 |
| Ukraine | Брюховичі | 0 | 0 | 2 |
| Ukraine | Буковина | 1 | 1 | 0 |
| Ukraine | Буськ | 1 | 1 | 0 |
| Ukraine | Бучали | 1 | 1 | 0 |
| Ukraine | Більче | 1 | 1 | 0 |
| Ukraine | Бісковичі | 1 | 1 | 0 |
| Ukraine | Велика Калинка | 1 | 1 | 0 |
| Ukraine | Великосілки | 1 | 1 | 0 |
| Ukraine | Великі Глібовичі | 1 | 1 | 0 |
| Ukraine | Вербиця | 1 | 1 | 0 |
| Ukraine | Верхня Рожанка | 1 | 1 | 0 |
| Ukraine | Викоти | 1 | 1 | 0 |
| Ukraine | Вовчатичі | 1 | 1 | 0 |
| Ukraine | Волиця | 2 | 2 | 0 |
| Ukraine | Волосянка | 1 | 1 | 0 |
| Ukraine | Волсвин | 1 | 1 | 0 |
| Ukraine | Воля | 1 | 1 | 0 |
| Ukraine | Воля-Довголуцька | 1 | 1 | 0 |
| Ukraine | Вороблевичі | 1 | 1 | 0 |
| Ukraine | Вороців | 2 | 2 | 0 |
| Ukraine | Вузлове | 2 | 2 | 0 |
| Ukraine | Вінниця | 323 | 323 | 0 |
| Ukraine | Вістовичі | 1 | 1 | 0 |
| Ukraine | Гамаліївка | 1 | 1 | 0 |
| Ukraine | Глинськ | 1 | 1 | 0 |
| Ukraine | Головецько | 2 | 2 | 0 |
| Ukraine | Гончарівка | 1 | 1 | 0 |
| Ukraine | Городище | 2 | 2 | 0 |
| Ukraine | Грусятичі | 1 | 1 | 0 |
| Ukraine | Грімне | 2 | 2 | 0 |
| Ukraine | Гірське | 1 | 1 | 0 |
| Ukraine | Давидів | 1 | 1 | 0 |
| Ukraine | Демня | 1 | 1 | 0 |
| Ukraine | Дніпро | 837 | 837 | 0 |
| Ukraine | Добромиль | 1 | 1 | 0 |
| Ukraine | Добротвір | 1 | 1 | 0 |
| Ukraine | Добрячин | 3 | 3 | 0 |
| Ukraine | Добрівляни | 1 | 1 | 0 |
| Ukraine | Долішнє | 1 | 1 | 0 |
| Ukraine | Домажир | 1 | 1 | 0 |
| Ukraine | Дрогобич | 3 | 3 | 0 |
| Ukraine | Дроговиж | 2 | 2 | 0 |
| Ukraine | Дубляни | 1 | 1 | 0 |
| Ukraine | Дуліби | 1 | 1 | 0 |
| Ukraine | Жвирка | 1 | 1 | 0 |
| Ukraine | Жидачів | 1 | 1 | 0 |
| Ukraine | Житомир | 134 | 134 | 0 |
| Ukraine | Жовква | 3 | 3 | 0 |
| Ukraine | Жорниська | 1 | 1 | 0 |
| Ukraine | Жуличі | 1 | 1 | 0 |
| Ukraine | Жупани | 1 | 1 | 0 |
| Ukraine | Журавків | 1 | 1 | 0 |
| Ukraine | Журавно | 2 | 2 | 0 |
| Ukraine | Заболотівці | 2 | 2 | 0 |
| Ukraine | Загірочко | 1 | 1 | 0 |
| Ukraine | Задністряни | 1 | 1 | 0 |
| Ukraine | Заліски | 1 | 1 | 0 |
| Ukraine | Замок | 1 | 1 | 0 |
| Ukraine | Заплатин | 1 | 1 | 0 |
| Ukraine | Запоріжжя | 422 | 422 | 0 |
| Ukraine | Зимна Вода | 2 | 2 | 0 |
| Ukraine | Зозулі | 1 | 1 | 0 |
| Ukraine | Золотковичі | 1 | 1 | 0 |
| Ukraine | Золочів | 1 | 1 | 0 |
| Ukraine | Зоротовичі | 2 | 2 | 0 |
| Ukraine | Зіболки | 1 | 1 | 0 |
| Ukraine | Кам’янка-Бузька | 3 | 3 | 0 |
| Ukraine | Катериничі | 1 | 1 | 0 |
| Ukraine | Керниця | 1 | 1 | 0 |
| Ukraine | Київ | 617 | 617 | 18 |
| Ukraine | Кожичі | 1 | 1 | 0 |
| Ukraine | Колбаєвичі | 1 | 1 | 0 |
| Ukraine | Конопниця | 1 | 1 | 0 |
| Ukraine | Конюшки | 1 | 1 | 0 |
| Ukraine | Кореличі | 2 | 2 | 0 |
| Ukraine | Корчин | 3 | 3 | 0 |
| Ukraine | Корчівка | 1 | 1 | 0 |
| Ukraine | Криве | 1 | 1 | 0 |
| Ukraine | Куликів | 1 | 1 | 0 |
| Ukraine | Куровичі | 1 | 1 | 0 |
| Ukraine | Лани | 1 | 1 | 0 |
| Ukraine | Лапшин | 1 | 1 | 0 |
| Ukraine | Летня | 1 | 1 | 0 |
| Ukraine | Липівці | 1 | 1 | 0 |
| Ukraine | Лопатин | 1 | 1 | 0 |
| Ukraine | Лучиці | 1 | 1 | 0 |
| Ukraine | Львів | 0 | 0 | 8 |
| Ukraine | Любша | 1 | 1 | 0 |
| Ukraine | Лівчиці | 1 | 1 | 0 |
| Ukraine | Ліщини | 1 | 1 | 0 |
| Ukraine | Малі Передримихи | 1 | 1 | 0 |
| Ukraine | Матів | 1 | 1 | 0 |
| Ukraine | Меденичі | 1 | 1 | 0 |
| Ukraine | Межиріччя | 1 | 1 | 0 |
| Ukraine | Миклашів | 1 | 1 | 0 |
| Ukraine | Миколаїв | 280 | 280 | 0 |
| Ukraine | Михайлевичі | 1 | 1 | 0 |
| Ukraine | Молодинче | 1 | 1 | 0 |
| Ukraine | Мочеради | 1 | 1 | 0 |
| Ukraine | Муроване | 1 | 1 | 0 |
| Ukraine | Міженець | 2 | 2 | 0 |
| Ukraine | Нижня Рожанка | 1 | 1 | 0 |
| Ukraine | Нижнє Синьовидне | 1 | 1 | 0 |
| Ukraine | Нова Скварява | 1 | 1 | 0 |
| Ukraine | Новий Витків | 1 | 1 | 0 |
| Ukraine | Новий Калинів | 1 | 1 | 0 |
| Ukraine | Новий Милятин | 2 | 2 | 0 |
| Ukraine | Новий Яричів | 2 | 2 | 0 |
| Ukraine | Оброшине | 2 | 2 | 0 |
| Ukraine | Одеса | 366 | 366 | 0 |
| Ukraine | Ожидів | 1 | 1 | 0 |
| Ukraine | Опори | 1 | 1 | 0 |
| Ukraine | Острів | 1 | 1 | 0 |
| Ukraine | Павлів | 1 | 1 | 0 |
| Ukraine | Паланки | 1 | 1 | 0 |
| Ukraine | Перекалки | 1 | 1 | 0 |
| Ukraine | Перемишляни | 2 | 2 | 0 |
| Ukraine | Пиняни | 1 | 1 | 0 |
| Ukraine | Плеників | 1 | 1 | 0 |
| Ukraine | Поздимир | 1 | 1 | 0 |
| Ukraine | Полове | 1 | 1 | 0 |
| Ukraine | Полтава | 300 | 300 | 0 |
| Ukraine | Поляни | 1 | 1 | 0 |
| Ukraine | Поріччя Задвірне | 1 | 1 | 0 |
| Ukraine | Поріччя-Грунтове | 1 | 1 | 0 |
| Ukraine | Поториця | 1 | 1 | 0 |
| Ukraine | Прибужани | 2 | 2 | 0 |
| Ukraine | Присліп | 1 | 1 | 0 |
| Ukraine | Пустомити | 1 | 1 | 0 |
| Ukraine | Пшонець | 1 | 1 | 0 |
| Ukraine | Підберізці | 2 | 2 | 0 |
| Ukraine | Підгайчики | 1 | 1 | 0 |
| Ukraine | Підгородці | 1 | 1 | 0 |
| Ukraine | Підкамінь | 1 | 1 | 0 |
| Ukraine | Підліски | 1 | 1 | 0 |
| Ukraine | Рава-Руська | 1 | 1 | 0 |
| Ukraine | Раделичі | 1 | 1 | 0 |
| Ukraine | Радехів | 1 | 1 | 0 |
| Ukraine | Ралівка | 2 | 2 | 0 |
| Ukraine | Руда | 1 | 1 | 0 |
| Ukraine | Рівне | 103 | 103 | 0 |
| Ukraine | Ріпнів | 2 | 2 | 0 |
| Ukraine | Річки | 1 | 1 | 0 |
| Ukraine | Садове товариство «Калійник» міста Стебник | 1 | 1 | 0 |
| Ukraine | Садове товариство «Мрія» | 1 | 1 | 0 |
| Ukraine | Садове товариство «Роздільне» | 1 | 1 | 0 |
| Ukraine | Сасів | 1 | 1 | 0 |
| Ukraine | Свитазів | 1 | 1 | 0 |
| Ukraine | Семенівка | 1 | 1 | 0 |
| Ukraine | Синьків | 1 | 1 | 0 |
| Ukraine | Скварява | 1 | 1 | 0 |
| Ukraine | Смереків | 1 | 1 | 0 |
| Ukraine | Сокаль | 3 | 3 | 0 |
| Ukraine | Соколів | 1 | 1 | 0 |
| Ukraine | Сокільники | 1 | 1 | 0 |
| Ukraine | Соснівка | 1 | 1 | 0 |
| Ukraine | Ставчани | 1 | 1 | 0 |
| Ukraine | Станин | 1 | 1 | 0 |
| Ukraine | Старе Село | 1 | 1 | 0 |
| Ukraine | Старий Добротвір | 1 | 1 | 0 |
| Ukraine | Старий Самбір | 1 | 1 | 0 |
| Ukraine | Стебник | 1 | 1 | 0 |
| Ukraine | Стороневичі | 1 | 1 | 0 |
| Ukraine | Струтин | 1 | 1 | 0 |
| Ukraine | Стрілки | 1 | 1 | 0 |
| Ukraine | Стрілковичі | 1 | 1 | 0 |
| Ukraine | Сугрів | 1 | 1 | 0 |
| Ukraine | Суми | 258 | 258 | 0 |
| Ukraine | Сілець | 1 | 1 | 0 |
| Ukraine | Тамановичі | 1 | 1 | 0 |
| Ukraine | Тершаків | 1 | 1 | 0 |
| Ukraine | Торки | 1 | 1 | 0 |
| Ukraine | Тулиголове | 1 | 1 | 0 |
| Ukraine | Туринка | 1 | 1 | 0 |
| Ukraine | Туркотин | 1 | 1 | 0 |
| Ukraine | Тухля | 1 | 1 | 0 |
| Ukraine | Тщенець | 1 | 1 | 0 |
| Ukraine | Утішків | 1 | 1 | 0 |
| Ukraine | Харків | 807 | 807 | 0 |
| Ukraine | Ходорів | 1 | 1 | 0 |
| Ukraine | Червоноград | 4 | 4 | 0 |
| Ukraine | Черкаси | 191 | 191 | 0 |
| Ukraine | Черляни | 1 | 1 | 0 |
| Ukraine | Черлянське Передмістя | 1 | 1 | 0 |
| Ukraine | Чернилява | 1 | 1 | 0 |
| Ukraine | Чернігів | 235 | 235 | 0 |
| Ukraine | Шегині | 1 | 1 | 0 |
| Ukraine | Юшківці | 2 | 2 | 0 |
| Ukraine | Яворів | 3 | 3 | 0 |
| Ukraine | Ямпіль | 1 | 1 | 0 |
| Ukraine | Ясениця-Сільна | 1 | 1 | 0 |
| Ukraine | Ясенівці | 1 | 1 | 0 |
| Ukraine | садове товариство «Явір» | 1 | 1 | 0 |
| Poland | Kraków | 6 | 6 | 0 |
| Poland | Warszawa | 56 | 112 | 0 |
| Poland | Wrocław | 749 | 749 | 0 |
| Poland | Łódź | 151 | 176 | 0 |
| South Africa | Cape Town | 8 | 8 | 3 |
| South Africa | Durban | 45 | 45 | 4 |
| South Africa | Johannesburg | 1 | 1 | 0 |
| South Africa | Pretoria | 27 | 27 | 2 |
| Vietnam | Hồ Chí Minh City | 3 | 3 | 2 |
| Kazakhstan | Алматы | 174 | 174 | 0 |
| Kazakhstan | Астана | 1 | 1 | 0 |
| Kazakhstan | Шымкент | 171 | 171 | 1 |
| India | Chennai | 0 | 0 | 1 |
| India | Kolkata | 1 | 1 | 1 |
| India | New Delhi | 7 | 7 | 0 |
| Uzbekistan | Ташкент | 656 | 656 | 0 |
| Lithuania | Vilnius | 1173 | 1173 | 0 |
| Czechia | Brno | 510 | 510 | 0 |
| Moldova | Chișinău | 622 | 622 | 0 |
| Estonia | Tallinn | 101 | 101 | 0 |

## Sources imported

- [kyiv](https://minio.kyivcity.gov.ua/kyivcity/sites/21/uploaded-files/Perelik%20pereimenovanykh%20u%202014-2025%20rokakh%20vulyts%20mista%20Kyieva.pdf) — retrieved 2026-11-14T05:29:14.327562+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [lviv-browser](https://loda.gov.ua/documents/111759) — retrieved 2026-11-14T05:39:00+00:00; CC BY 4.0, as stated in the official page footer. Attribution: Lviv Regional Military Administration.
- [Kharkiv regional administration order 513 В, 26 July 2024](https://kharkivoda.gov.ua/content/documents/1277/127689/files/%D0%BC%D1%96%D1%81%D1%82%D0%BE%20%D0%A5%D0%B0%D1%80%D0%BA%D1%96%D0%B2.PDF) — retrieved 2026-11-14T06:33:20.301039+00:00; Factual mappings only; source retained for audit, not republished. No blanket reuse licence established.
- [lviv-appendix2-browser](https://loda.gov.ua/documents/111760) — retrieved 2026-11-14T17:55:32.085281+00:00; CC BY 4.0 per source footer. Attribution: Lviv Regional Military Administration.
- [Ukrposhta street address classifier: Дніпро](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_street_by_region_id_and_district_id_and_city_id_and_street_ua&region_id=264&district_id=301&city_id=3641&street_ua=) — retrieved 2026-11-14T18:19:50.283569+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta street address classifier: Харків](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_street_by_region_id_and_district_id_and_city_id_and_street_ua&region_id=280&district_id=395&city_id=24550&street_ua=) — retrieved 2026-11-14T18:22:40.815700+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta street address classifier: Одеса](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_street_by_region_id_and_district_id_and_city_id_and_street_ua&region_id=275&district_id=371&city_id=17069&street_ua=) — retrieved 2026-11-14T18:25:12.398557+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta street address classifier: Запоріжжя](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_street_by_region_id_and_district_id_and_city_id_and_street_ua&region_id=268&district_id=328&city_id=8968&street_ua=) — retrieved 2026-11-14T18:25:15.132488+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta street address classifier: Вінниця](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_street_by_region_id_and_district_id_and_city_id_and_street_ua&region_id=262&district_id=291&city_id=1057&street_ua=) — retrieved 2026-11-14T18:28:57.156527+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta street address classifier: Полтава](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_street_by_region_id_and_district_id_and_city_id_and_street_ua&region_id=276&district_id=377&city_id=19234&street_ua=) — retrieved 2026-11-14T18:28:59.331262+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta street address classifier: Чернігів](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_street_by_region_id_and_district_id_and_city_id_and_street_ua&region_id=285&district_id=418&city_id=29712&street_ua=) — retrieved 2026-11-14T18:29:02.130926+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta street address classifier: Черкаси](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_street_by_region_id_and_district_id_and_city_id_and_street_ua&region_id=283&district_id=408&city_id=27760&street_ua=) — retrieved 2026-11-14T18:29:05.560443+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta street address classifier: Миколаїв](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_street_by_region_id_and_district_id_and_city_id_and_street_ua&region_id=274&district_id=365&city_id=16169&street_ua=) — retrieved 2026-11-14T18:32:52.627747+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta street address classifier: Житомир](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_street_by_region_id_and_district_id_and_city_id_and_street_ua&region_id=266&district_id=317&city_id=6708&street_ua=) — retrieved 2026-11-14T18:32:57.734525+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta street address classifier: Рівне](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_street_by_region_id_and_district_id_and_city_id_and_street_ua&region_id=277&district_id=380&city_id=20296&street_ua=) — retrieved 2026-11-14T18:32:59.655277+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta street address classifier: Суми](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_street_by_region_id_and_district_id_and_city_id_and_street_ua&region_id=278&district_id=385&city_id=21680&street_ua=) — retrieved 2026-11-14T18:33:00.965737+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [warsaw1](https://warszawa19115.pl/documents/20184/17793521/Wykaz%20nr%201%20-%20Rada%20Miasta%206%20ulic%20%289%2C7%20kB%29.xlsx) — retrieved 2026-11-14T05:29:17.305724+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [warsaw2](https://warszawa19115.pl/documents/20184/17793521/Wykaz%20nr%202%20Dekomunizacja%20%2818%2C4%20kB%29.xlsx) — retrieved 2026-11-14T05:29:14.328887+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [krakow-law](https://edziennik.malopolska.uw.gov.pl/WDU_K/2017/5597/akt.pdf) — retrieved 2026-11-14T05:41:41.578526+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: w](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-w/) — retrieved 2026-11-14T06:35:49.567078+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: t](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-t/) — retrieved 2026-11-14T06:35:48.128246+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: g](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-g/) — retrieved 2026-11-14T06:35:40.941007+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: o](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-o/) — retrieved 2026-11-14T06:35:45.222566+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: u](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-u/) — retrieved 2026-11-14T06:35:49.188199+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: k](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-k/) — retrieved 2026-11-14T06:35:43.097130+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: d](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-d/) — retrieved 2026-11-14T06:35:39.495384+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: z](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-z/) — retrieved 2026-11-14T06:35:50.457077+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: p](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-p/) — retrieved 2026-11-14T06:35:46.758491+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: b](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-b/) — retrieved 2026-11-14T06:35:36.461338+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: f](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-f/) — retrieved 2026-11-14T06:35:40.581920+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: s](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-s/) — retrieved 2026-11-14T06:35:47.137492+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: e](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-e/) — retrieved 2026-11-14T06:35:39.817144+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: j](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-j/) — retrieved 2026-11-14T06:35:42.383986+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: 2](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-s-2/) — retrieved 2026-11-14T06:35:47.849239+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: h](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-h/) — retrieved 2026-11-14T06:35:41.202672+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: r](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-r/) — retrieved 2026-11-14T06:35:46.441937+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: 2](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-l-2/) — retrieved 2026-11-14T06:35:43.802027+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: 3](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-z-3/) — retrieved 2026-11-14T06:35:50.938949+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: l](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-l/) — retrieved 2026-11-14T06:35:43.423363+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: a](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-a/) — retrieved 2026-11-14T06:35:36.399269+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: i](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-i/) — retrieved 2026-11-14T06:35:42.012757+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: c](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-c/) — retrieved 2026-11-14T06:35:36.249139+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: m](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-m/) — retrieved 2026-11-14T06:35:44.761753+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [Łódzki Ośrodek Geodezji municipal naming dictionary: n](https://log.lodz.pl/slownik-nazewnictwa-miejskiego/slownik-n/) — retrieved 2026-11-14T06:35:44.828852+00:00; Factual mappings only; dictionary prose retained locally for audit, not republished.
- [lodz-current-register](https://log.lodz.pl/mapy-i-uslugi-online/ulice/) — retrieved 2026-11-14T17:56:49.907405+00:00; Factual current street names only; captured for audit.
- [durban](https://visitdurban.travel/storage/Destination%20Durban%20Visitor%20Guide%202025%20web.pdf) — retrieved 2026-11-14T05:29:14.334102+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [pretoria](https://www.treasury.gov.za/nt/PTA%20Central%20New%20Street%20Names.pdf) — retrieved 2026-11-14T05:30:11.102182+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [johannesburg](https://joburg.org.za/documents_/Documents/City-of-Johannesburg-Integrated-Annual-Report_2023.24.pdf) — retrieved 2026-11-14T05:30:15.809699+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [City of Cape Town Language Style Guide, street name changes](https://www.etenders.gov.za/home/Download/?blobName=7bd24859-347c-480c-9aec-4bd2c803fd17.pdf&downloadedFileName=Annexure+B+Language_Style_Guide5_2017.pdf) — retrieved 2026-11-14T06:33:20.308573+00:00; Factual mappings only; source retained for audit, not republished. No blanket reuse licence established.
- [Tshwane visitor attractions map, Renamed Streets table](https://www.discovertshwane.com/wp-content/uploads/2021/03/Tshwane-Attractions-Map.pdf) — retrieved 2026-11-14T06:33:20.499253+00:00; Factual mappings only; source retained for audit, not republished. No blanket reuse licence established.
- [hcmc-gov](https://tphcm.chinhphu.vn/xa-lo-ha-noi-chinh-thuc-khoac-ten-moi-101230823115413686.htm) — retrieved 2026-11-14T05:30:11.110160+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [saigon-dongkhoi](https://vnexpress.net/tp-hcm-xua-va-nay-qua-cac-dia-diem-lich-su-nam-1975-4881143.html) — retrieved 2026-11-14T05:45:27.521406+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [saigon-current](https://vietnam.travel/places-to-go/southern-vietnam/ho-chi-minh-city/) — retrieved 2026-11-14T05:45:27.520823+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [almaty](https://old.adilet.zan.kz/rus/docs/V24R0002332) — retrieved 2026-11-14T05:29:14.340812+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [astana](https://old.adilet.zan.kz/rus/docs/G24ABW51124) — retrieved 2026-11-14T05:30:11.100848+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [almaty2018](https://old.adilet.zan.kz/rus/docs/V18R0001521) — retrieved 2026-11-14T05:39:47.623916+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [shymkent-2014](https://old.adilet.zan.kz/rus/docs/V14U0002942) — retrieved 2026-11-14T17:54:19.676670+00:00; Factual mappings only; captured source retained for audit, not served publicly.
- [delhi](https://ndmc.gov.in/council/Resolutions%202007/year%20wise/2017/ITEM%20No%2001%20%28T-04%29-2017.pdf) — retrieved 2026-11-14T05:29:14.337104+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [chennai](https://chennaicorporation.gov.in/gcc/images/Chennai%20U%20A%20%20City%20Action%20plan.pdf) — retrieved 2026-11-14T05:30:12.007608+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [kartavya-pib](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1857900&lang=2&reg=48) — retrieved 2026-11-14T05:39:09.750161+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [delhi2017](https://ndmc.gov.in/council/Resolutions%202007/year%20wise/2017/Council%20Meeting%20No%2015-2016-2017-V-I.pdf) — retrieved 2026-11-14T05:39:12.216355+00:00; No explicit reuse licence established; factual name mappings only; source documents retained for audit, not served publicly.
- [Kolkata Municipal Corporation newsletter June 2017](https://www.kmcgov.in/KMCPortal/downloads/EletterJun2017_04_07_2017.pdf) — retrieved 2026-11-14T06:33:20.793640+00:00; Factual mappings only; source retained for audit, not republished. No blanket reuse licence established.
- [B. P. Hasdeu Municipal Library: Chișinău boulevards, streets, squares and parks encyclopedic guide](https://hapes.hasdeu.md/bitstream/handle/123456789/399/Chi%C8%99in%C4%83u%20Bulevarde%2C%20str%C4%83zi%2C%20pie%C8%9Be%2C%20parcuri_Ghid%20enciclopedic.pdf?isAllowed=y&sequence=1) — retrieved 2026-11-14T18:55:43.927602+00:00; Factual mappings only; capture retained for source audit, not served publicly.
- [Institute of the Estonian Language: Tallinn renamed streets, 1987–2018](https://arhiiv.eki.ee/knab/tallinn2.htm) — retrieved 2026-11-14T18:55:43.929034+00:00; Factual mappings only; capture retained for source audit, not served publicly.
- [Institute of the Estonian Language: Tallinn street-name inventory, 2018](https://arhiiv.eki.ee/knab/tallinn1.htm) — retrieved 2026-11-14T18:55:43.932371+00:00; Factual mappings only; capture retained for source audit, not served publicly.
- [Golden Pages Uzbekistan: former and new Tashkent street names (directory, not a legal register)](https://www.goldenpages.uz/streets/) — retrieved 2026-11-14T18:44:38.962536+00:00; Factual mappings only; capture retained for source audit, not served publicly.
- [WroclawGuide: historical German and present Polish street-name pairs](https://www.wroclawguide.com/en/old-german-street-names-in-breslau-wroclaw/) — retrieved 2026-11-14T18:46:24.518091+00:00; Factual mappings only; capture retained for source audit, not served publicly.
- [City of Wrocław EMUiA current street-name register](https://geoportal.wroclaw.pl/www/emuia/Ulice.zip) — retrieved 2026-11-14T18:46:24.519761+00:00; Factual mappings only; capture retained for source audit, not served publicly.
- [About Vilnius: present, pre-1987 and historical street-name table (2007, supplemented)](https://vilnius.penki.lt/ulicy_vilniusa) — retrieved 2026-11-14T18:51:08.927437+00:00; Factual mappings only; capture retained for source audit, not served publicly.
- [Hnit-Baltic Lithuania road dataset: Vilnius street names and address-register codes](https://utility.arcgis.com/usrsvcs/servers/087d2b1b6b244c31be0d060c7f7bdb09/rest/services/Hosted/Keiai_gatves/FeatureServer/0/query?f=json&where=gyv_pavad+%3D+%27Vilniaus+m.%27&outFields=vardas%2Cgat_kodas%2Cgyv_pavad&returnGeometry=false&returnDistinctValues=true&orderByFields=vardas%2Cgat_kodas&resultRecordCount=2000&resultOffset=0) — retrieved 2026-11-14T18:52:43.333394+00:00; Factual name attributes only; underlying Address Register attribution: VĮ Registrų centras, CC BY 4.0. No geometry republished.
- [Hnit-Baltic Lithuania road dataset: Vilnius street names and address-register codes](https://utility.arcgis.com/usrsvcs/servers/087d2b1b6b244c31be0d060c7f7bdb09/rest/services/Hosted/Keiai_gatves/FeatureServer/0/query?f=json&where=gyv_pavad+%3D+%27Vilniaus+m.%27&outFields=vardas%2Cgat_kodas%2Cgyv_pavad&returnGeometry=false&returnDistinctValues=true&orderByFields=vardas%2Cgat_kodas&resultRecordCount=2000&resultOffset=2000) — retrieved 2026-11-14T18:52:44.464989+00:00; Factual name attributes only; underlying Address Register attribution: VĮ Registrų centras, CC BY 4.0. No geometry republished.
- [Encyclopedia of Brno: Akátová](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=47) — retrieved 2026-11-14T18:53:24+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 1](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=0&page_total=64) — retrieved 2026-11-14T18:58:52.137835+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Amerlingova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=115) — retrieved 2026-11-14T18:53:25+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Andrýskova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=123) — retrieved 2026-11-14T18:53:25+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Antala Staška](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=131) — retrieved 2026-11-14T18:53:25+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Antonína Macka](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=140) — retrieved 2026-11-14T18:53:26+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Antonína Procházky](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=142) — retrieved 2026-11-14T18:53:26+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Antonína Slavíka](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=143) — retrieved 2026-11-14T18:53:26+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Antonínská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=146) — retrieved 2026-11-14T18:53:27+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Arne Nováka](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=174) — retrieved 2026-11-14T18:53:27+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Auerswaldova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=183) — retrieved 2026-11-14T18:53:27+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Baarovo nábřeží](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=231) — retrieved 2026-11-14T18:53:29+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Babická](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=237) — retrieved 2026-11-14T18:53:29+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Babičkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=239) — retrieved 2026-11-14T18:53:29+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Banskobystrická](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=265) — retrieved 2026-11-14T18:53:30+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 2](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=1&page_total=64) — retrieved 2026-11-14T18:58:52.140003+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Barvičova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=284) — retrieved 2026-11-14T18:53:31+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Barvířská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=285) — retrieved 2026-11-14T18:53:31+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bašty](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=851) — retrieved 2026-11-14T18:53:31+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bauerova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=301) — retrieved 2026-11-14T18:53:32+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bayerova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=305) — retrieved 2026-11-14T18:53:32+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bednaříkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=308) — retrieved 2026-11-14T18:53:32+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bednářova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=309) — retrieved 2026-11-14T18:53:32+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bedřichovická](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=317) — retrieved 2026-11-14T18:53:33+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Beethovenova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=318) — retrieved 2026-11-14T18:53:33+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Běhounská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=321) — retrieved 2026-11-14T18:53:33+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Belcrediho](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=409) — retrieved 2026-11-14T18:53:33+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bělidla](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=411) — retrieved 2026-11-14T18:53:34+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bělohorská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=414) — retrieved 2026-11-14T18:53:34+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Berkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=430) — retrieved 2026-11-14T18:53:35+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bernáčkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=431) — retrieved 2026-11-14T18:53:35+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Besední](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=432) — retrieved 2026-11-14T18:53:36+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Gorkého](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1425) — retrieved 2026-11-14T18:54:30+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 11](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=10&page_total=64) — retrieved 2026-11-14T18:58:52.152385+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Grmelova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1455) — retrieved 2026-11-14T18:54:30+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Grohova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1456) — retrieved 2026-11-14T18:54:30+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Gromešova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1459) — retrieved 2026-11-14T18:54:30+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Haasova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1482) — retrieved 2026-11-14T18:54:31+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hájecká](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1495) — retrieved 2026-11-14T18:54:33+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hamry](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1517) — retrieved 2026-11-14T18:54:34+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hapalova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1537) — retrieved 2026-11-14T18:54:34+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Haraštova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1538) — retrieved 2026-11-14T18:54:35+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Havelkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1563) — retrieved 2026-11-14T18:54:36+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Havlenova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1566) — retrieved 2026-11-14T18:54:36+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Havlišova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1589) — retrieved 2026-11-14T18:54:36+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 12](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=11&page_total=64) — retrieved 2026-11-14T18:58:52.153605+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Havraní](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1590) — retrieved 2026-11-14T18:54:37+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Havránkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1591) — retrieved 2026-11-14T18:54:37+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Heinrichova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1601) — retrieved 2026-11-14T18:54:37+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Helceletova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1604) — retrieved 2026-11-14T18:54:37+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Helenčina](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1606) — retrieved 2026-11-14T18:54:38+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Helfertova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1608) — retrieved 2026-11-14T18:54:38+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Herbenova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1615) — retrieved 2026-11-14T18:54:38+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hermannova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1628) — retrieved 2026-11-14T18:54:39+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Heršpická](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1637) — retrieved 2026-11-14T18:54:39+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Heydukova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1647) — retrieved 2026-11-14T18:54:39+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hilleho](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1651) — retrieved 2026-11-14T18:54:40+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hladíkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1690) — retrieved 2026-11-14T18:54:40+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hlaváčova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1696) — retrieved 2026-11-14T18:54:40+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hlávkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1699) — retrieved 2026-11-14T18:54:41+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hlídka](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1707) — retrieved 2026-11-14T18:54:41+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hlinky](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1710) — retrieved 2026-11-14T18:54:41+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hněvkovského](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1716) — retrieved 2026-11-14T18:54:42+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hoblíkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1717) — retrieved 2026-11-14T18:54:43+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hodonínská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1718) — retrieved 2026-11-14T18:54:43+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 13](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=12&page_total=64) — retrieved 2026-11-14T18:58:52.154813+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Holzova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1751) — retrieved 2026-11-14T18:54:45+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hoppova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1757) — retrieved 2026-11-14T18:54:45+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Horákova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1760) — retrieved 2026-11-14T18:54:45+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Horákovská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1762) — retrieved 2026-11-14T18:54:46+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Horova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1785) — retrieved 2026-11-14T18:54:46+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Horymírova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1793) — retrieved 2026-11-14T18:54:47+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hořejší](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1794) — retrieved 2026-11-14T18:54:47+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hostinského](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1795) — retrieved 2026-11-14T18:54:47+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hostislavova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1796) — retrieved 2026-11-14T18:54:48+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hoštická](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1799) — retrieved 2026-11-14T18:54:48+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Houbalova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1805) — retrieved 2026-11-14T18:54:48+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hradecká](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1811) — retrieved 2026-11-14T18:54:49+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hradilova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1812) — retrieved 2026-11-14T18:54:49+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hradiska](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1813) — retrieved 2026-11-14T18:54:49+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hraničky](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1814) — retrieved 2026-11-14T18:54:49+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hrdličkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1824) — retrieved 2026-11-14T18:54:50+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 14](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=13&page_total=64) — retrieved 2026-11-14T18:58:52.156386+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hrnčířská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1826) — retrieved 2026-11-14T18:54:50+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hromádkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1829) — retrieved 2026-11-14T18:54:51+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hroznová](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1834) — retrieved 2026-11-14T18:54:51+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hrubého](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1835) — retrieved 2026-11-14T18:54:51+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hrubinky](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1836) — retrieved 2026-11-14T18:54:51+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hudcova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1852) — retrieved 2026-11-14T18:54:53+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hujíčkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1854) — retrieved 2026-11-14T18:54:53+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Humenná](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1857) — retrieved 2026-11-14T18:54:53+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Husitská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1873) — retrieved 2026-11-14T18:54:53+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Húskova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1874) — retrieved 2026-11-14T18:54:53+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Husovická](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1890) — retrieved 2026-11-14T18:54:54+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hutařova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1908) — retrieved 2026-11-14T18:54:54+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hvězdárenská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1919) — retrieved 2026-11-14T18:54:54+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Hvězdová](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1921) — retrieved 2026-11-14T18:54:55+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Chaloupkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1940) — retrieved 2026-11-14T18:54:56+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Chaloupky](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1941) — retrieved 2026-11-14T18:54:56+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Charbulova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1943) — retrieved 2026-11-14T18:54:56+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Charvatská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1947) — retrieved 2026-11-14T18:54:57+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 15](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=14&page_total=64) — retrieved 2026-11-14T18:58:52.157553+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Chelčického](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1948) — retrieved 2026-11-14T18:54:57+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Chládkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1952) — retrieved 2026-11-14T18:54:57+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Chleborádova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1953) — retrieved 2026-11-14T18:54:57+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Chodská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1960) — retrieved 2026-11-14T18:54:59+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Chrlické náměstí](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1968) — retrieved 2026-11-14T18:54:59+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Chrpová](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1969) — retrieved 2026-11-14T18:55:00+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Chudobova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1970) — retrieved 2026-11-14T18:55:00+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Churého](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1971) — retrieved 2026-11-14T18:55:00+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Ibsenova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1974) — retrieved 2026-11-14T18:55:01+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Ivanovické náměstí](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2042) — retrieved 2026-11-14T18:55:01+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jablonského](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2047) — retrieved 2026-11-14T18:55:02+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jahodová](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2054) — retrieved 2026-11-14T18:55:02+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jakubská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2059) — retrieved 2026-11-14T18:55:02+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jakubské náměstí](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2061) — retrieved 2026-11-14T18:55:03+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jamborova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2063) — retrieved 2026-11-14T18:55:03+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jana Broskvy](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2066) — retrieved 2026-11-14T18:55:04+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 16](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=15&page_total=64) — retrieved 2026-11-14T18:58:52.158686+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jana Nečase](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2071) — retrieved 2026-11-14T18:55:04+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jana Svobody](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2073) — retrieved 2026-11-14T18:55:04+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jana Uhra](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2074) — retrieved 2026-11-14T18:55:04+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Janáčkovo náměstí](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2079) — retrieved 2026-11-14T18:55:04+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jandáskova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2081) — retrieved 2026-11-14T18:55:05+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jánošíkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2084) — retrieved 2026-11-14T18:55:05+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Janouškova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2087) — retrieved 2026-11-14T18:55:05+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jánská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2092) — retrieved 2026-11-14T18:55:05+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jaselská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2104) — retrieved 2026-11-14T18:55:07+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jateční](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2108) — retrieved 2026-11-14T18:55:08+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Ječná](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2112) — retrieved 2026-11-14T18:55:08+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jedlová](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2113) — retrieved 2026-11-14T18:55:08+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jelínkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2120) — retrieved 2026-11-14T18:55:10+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jemelkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2121) — retrieved 2026-11-14T18:55:10+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jeneweinova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2123) — retrieved 2026-11-14T18:55:10+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jeníčkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2124) — retrieved 2026-11-14T18:55:10+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 17](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=16&page_total=64) — retrieved 2026-11-14T18:58:52.159698+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jeronýmova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2126) — retrieved 2026-11-14T18:55:11+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jeřábkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2128) — retrieved 2026-11-14T18:55:11+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jezerní](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2132) — retrieved 2026-11-14T18:55:12+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jezuitská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2134) — retrieved 2026-11-14T18:55:12+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jihlavská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2136) — retrieved 2026-11-14T18:55:12+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jilemnického](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2139) — retrieved 2026-11-14T18:55:13+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jílkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2140) — retrieved 2026-11-14T18:55:13+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jílová](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2141) — retrieved 2026-11-14T18:55:13+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jiránkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2145) — retrieved 2026-11-14T18:55:14+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jircháře](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2161) — retrieved 2026-11-14T18:55:14+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jiřinová](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2167) — retrieved 2026-11-14T18:55:15+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jižní náměstí](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2171) — retrieved 2026-11-14T18:55:15+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Josefská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2210) — retrieved 2026-11-14T18:55:16+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Joštova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2221) — retrieved 2026-11-14T18:55:16+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jubilejní](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2230) — retrieved 2026-11-14T18:55:17+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jugoslávská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2240) — retrieved 2026-11-14T18:55:17+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 18](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=17&page_total=64) — retrieved 2026-11-14T18:58:52.160709+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Juliánovské náměstí](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2243) — retrieved 2026-11-14T18:55:17+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Jundrovská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2250) — retrieved 2026-11-14T18:55:18+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: K Bukovinám](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2274) — retrieved 2026-11-14T18:55:19+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: K Lázinkám](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2279) — retrieved 2026-11-14T18:55:20+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: K Západi](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2288) — retrieved 2026-11-14T18:55:21+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Kabátníkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2290) — retrieved 2026-11-14T18:55:21+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Kaleckého](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2309) — retrieved 2026-11-14T18:55:21+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Kallabova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2313) — retrieved 2026-11-14T18:55:22+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Kaloudova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2315) — retrieved 2026-11-14T18:55:22+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Kalvodova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=2323) — retrieved 2026-11-14T18:55:23+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bezovka](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=436) — retrieved 2026-11-14T18:53:36+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 3](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=2&page_total=64) — retrieved 2026-11-14T18:58:52.141295+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bidláky](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=441) — retrieved 2026-11-14T18:53:37+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bílého](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=444) — retrieved 2026-11-14T18:53:38+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bílovická](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=446) — retrieved 2026-11-14T18:53:38+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Biskupská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=453) — retrieved 2026-11-14T18:53:38+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Blahoslavova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=464) — retrieved 2026-11-14T18:53:38+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Blatného](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=470) — retrieved 2026-11-14T18:53:39+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Blümlova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=482) — retrieved 2026-11-14T18:53:40+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Boettingrova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=490) — retrieved 2026-11-14T18:53:41+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bohatcova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=491) — retrieved 2026-11-14T18:53:41+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Böhmova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=496) — retrieved 2026-11-14T18:53:41+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bohunická](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=500) — retrieved 2026-11-14T18:53:42+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bochořákova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=503) — retrieved 2026-11-14T18:53:42+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bolzanova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=507) — retrieved 2026-11-14T18:53:42+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Borová](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=513) — retrieved 2026-11-14T18:53:43+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 4](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=3&page_total=64) — retrieved 2026-11-14T18:58:52.142977+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Botanická](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=527) — retrieved 2026-11-14T18:53:45+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Boženy Němcové](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=532) — retrieved 2026-11-14T18:53:45+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bráfova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=540) — retrieved 2026-11-14T18:53:46+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Brandlova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=546) — retrieved 2026-11-14T18:53:46+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bratislavská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=550) — retrieved 2026-11-14T18:53:46+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bratří Čapků](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=551) — retrieved 2026-11-14T18:53:47+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bratří Mrštíků](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=553) — retrieved 2026-11-14T18:53:47+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bratří Žůrků](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=557) — retrieved 2026-11-14T18:53:48+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Břeclavská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=621) — retrieved 2026-11-14T18:53:50+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 5](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=4&page_total=64) — retrieved 2026-11-14T18:58:52.144231+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Břehová](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=622) — retrieved 2026-11-14T18:53:50+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Břenkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=624) — retrieved 2026-11-14T18:53:50+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Břetislavova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=625) — retrieved 2026-11-14T18:53:50+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Březinova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=627) — retrieved 2026-11-14T18:53:51+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Březová](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=629) — retrieved 2026-11-14T18:53:51+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Budínská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=634) — retrieved 2026-11-14T18:53:52+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Budovcova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=636) — retrieved 2026-11-14T18:53:52+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Buchtova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=640) — retrieved 2026-11-14T18:53:52+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Buková](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=642) — retrieved 2026-11-14T18:53:53+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Bukovského](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=643) — retrieved 2026-11-14T18:53:53+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Burešova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=649) — retrieved 2026-11-14T18:53:53+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Burianovo náměstí](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=658) — retrieved 2026-11-14T18:53:53+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Cacovická](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=671) — retrieved 2026-11-14T18:53:55+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Cejl](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=682) — retrieved 2026-11-14T18:53:55+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Celní](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=685) — retrieved 2026-11-14T18:53:55+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Cihelní](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=688) — retrieved 2026-11-14T18:53:55+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Cihlářská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=689) — retrieved 2026-11-14T18:53:56+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Cimburkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=695) — retrieved 2026-11-14T18:53:56+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 6](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=5&page_total=64) — retrieved 2026-11-14T18:58:52.145428+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Colova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=712) — retrieved 2026-11-14T18:53:57+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Cornovova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=733) — retrieved 2026-11-14T18:53:57+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Ctiradova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=739) — retrieved 2026-11-14T18:53:57+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Cupákova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=740) — retrieved 2026-11-14T18:53:57+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Cyrilská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=744) — retrieved 2026-11-14T18:53:57+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Čápkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=755) — retrieved 2026-11-14T18:53:58+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Čechyňská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=775) — retrieved 2026-11-14T18:53:58+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Čejkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=776) — retrieved 2026-11-14T18:53:58+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Černopolní](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=799) — retrieved 2026-11-14T18:54:00+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Černovická](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=801) — retrieved 2026-11-14T18:54:01+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Černovičky](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=805) — retrieved 2026-11-14T18:54:01+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Černozemní](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=806) — retrieved 2026-11-14T18:54:02+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Červený kopec](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=809) — retrieved 2026-11-14T18:54:02+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Česká](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=813) — retrieved 2026-11-14T18:54:02+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dačického](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=822) — retrieved 2026-11-14T18:54:03+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 7](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=6&page_total=64) — retrieved 2026-11-14T18:58:52.146517+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dalimilova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=830) — retrieved 2026-11-14T18:54:04+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Demlova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=849) — retrieved 2026-11-14T18:54:05+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Denisovy sady](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=298) — retrieved 2026-11-14T18:54:05+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Desátková](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=853) — retrieved 2026-11-14T18:54:05+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Díly](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=865) — retrieved 2026-11-14T18:54:06+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Divadelní](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=867) — retrieved 2026-11-14T18:54:06+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Divišova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=876) — retrieved 2026-11-14T18:54:06+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dlážděná](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=886) — retrieved 2026-11-14T18:54:06+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dlouhé hony](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=892) — retrieved 2026-11-14T18:54:07+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Doležalova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=909) — retrieved 2026-11-14T18:54:08+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dolnice](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=931) — retrieved 2026-11-14T18:54:08+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dolnopolní](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=933) — retrieved 2026-11-14T18:54:08+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Domažlická](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=934) — retrieved 2026-11-14T18:54:08+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dominikánská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=938) — retrieved 2026-11-14T18:54:08+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dominikánské náměstí](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=939) — retrieved 2026-11-14T18:54:09+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dornych](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=950) — retrieved 2026-11-14T18:54:09+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dostálova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=953) — retrieved 2026-11-14T18:54:09+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Došlíkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=954) — retrieved 2026-11-14T18:54:10+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Drápelova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=998) — retrieved 2026-11-14T18:54:10+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 8](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=7&page_total=64) — retrieved 2026-11-14T18:58:52.147711+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Drdy](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1004) — retrieved 2026-11-14T18:54:10+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Drnovická](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1008) — retrieved 2026-11-14T18:54:11+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Drobného](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1011) — retrieved 2026-11-14T18:54:11+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Drozdí](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1012) — retrieved 2026-11-14T18:54:11+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dudíkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1028) — retrieved 2026-11-14T18:54:12+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dufkovo nábřeží](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1029) — retrieved 2026-11-14T18:54:12+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dukelská třída](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1031) — retrieved 2026-11-14T18:54:13+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dulánek](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1032) — retrieved 2026-11-14T18:54:13+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dunajská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1034) — retrieved 2026-11-14T18:54:14+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Durďákova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1035) — retrieved 2026-11-14T18:54:14+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dvorecká](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1037) — retrieved 2026-11-14T18:54:14+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dvorského](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1042) — retrieved 2026-11-14T18:54:14+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dvořiště](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1052) — retrieved 2026-11-14T18:54:15+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Dykova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1057) — retrieved 2026-11-14T18:54:15+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Ečerova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1066) — retrieved 2026-11-14T18:54:15+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Eimova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1072) — retrieved 2026-11-14T18:54:16+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Elgartova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1082) — retrieved 2026-11-14T18:54:16+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 9](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=8&page_total=64) — retrieved 2026-11-14T18:58:52.148961+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Eliášova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1083) — retrieved 2026-11-14T18:54:17+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Elišky Krásnohorské](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1093) — retrieved 2026-11-14T18:54:17+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Elplova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1096) — retrieved 2026-11-14T18:54:18+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Erbenova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1110) — retrieved 2026-11-14T18:54:18+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Ernsta Macha](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1114) — retrieved 2026-11-14T18:54:18+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Faměrovo náměstí](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1150) — retrieved 2026-11-14T18:54:18+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Farní](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1156) — retrieved 2026-11-14T18:54:19+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Farského](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1158) — retrieved 2026-11-14T18:54:19+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Faulhabrova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1163) — retrieved 2026-11-14T18:54:19+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Ferrerova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1190) — retrieved 2026-11-14T18:54:20+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Fibichova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1197) — retrieved 2026-11-14T18:54:20+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Filipínského](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1204) — retrieved 2026-11-14T18:54:20+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Fišova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1217) — retrieved 2026-11-14T18:54:22+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Florianova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1225) — retrieved 2026-11-14T18:54:22+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Foustkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1248) — retrieved 2026-11-14T18:54:23+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: current street index, page 10](https://encyklopedie.brna.cz/home-mmb/?json=next-page&cms_id=90&page_current=9&page_total=64) — retrieved 2026-11-14T18:58:52.150950+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Francouzská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1249) — retrieved 2026-11-14T18:54:23+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Františkánská](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1263) — retrieved 2026-11-14T18:54:24+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Františky Stránecké](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1267) — retrieved 2026-11-14T18:54:24+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Fryčajova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1337) — retrieved 2026-11-14T18:54:25+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Fučíkova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1340) — retrieved 2026-11-14T18:54:25+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Gajdošova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1356) — retrieved 2026-11-14T18:54:26+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Gallašova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1359) — retrieved 2026-11-14T18:54:26+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Gargulákova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1360) — retrieved 2026-11-14T18:54:27+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Gebauerova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1373) — retrieved 2026-11-14T18:54:27+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Geislerova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1379) — retrieved 2026-11-14T18:54:27+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Gellnerova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1381) — retrieved 2026-11-14T18:54:28+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Glocova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1406) — retrieved 2026-11-14T18:54:29+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Gogolova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1412) — retrieved 2026-11-14T18:54:29+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Encyclopedia of Brno: Gorazdova](https://encyklopedie.brna.cz/home-mmb/?acc=profil-ulice&load=1422) — retrieved 2026-11-14T18:54:29+00:00; Factual name mappings only; raw evidence retained for audit, not served publicly.
- [Verkhovna Rada of Ukraine](https://www.rada.gov.ua/en/news/News/top_news/131134.html) — retrieved 2026-11-14; Factual name mapping only. Source linked, not republished.
- [ukraine-renamed-cities](https://land.gov.ua/wp-content/uploads/2018/08/Перейменування_міста_ВРУ_28_08.pdf) — retrieved 2026-11-14T17:55:32.373201+00:00; Factual mappings only; captured source retained for audit, not served publicly.
- [United Nations Digital Library](https://digitallibrary.un.org/record/1282124) — retrieved 2026-11-14; Factual name mapping only. Source linked, not republished.
- [un-m49](https://unstats.un.org/unsd/methodology/m49/) — retrieved 2026-11-14T17:52:17.950854+00:00; Factual mappings only; captured source retained for audit, not served publicly.
- [karnataka-renames-browser](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/387496/Karnataka_State_India_Name_Changes_20141112.pdf) — retrieved 2026-11-14T17:58:21.557845+00:00; Crown copyright; factual mappings only. Source capture retained for audit.
- [india-factfile](https://assets.publishing.service.gov.uk/media/6ab67e78997a4b2950ccef41/India_Toponymic_Factfile.pdf) — retrieved 2026-11-14T17:54:32.313766+00:00; Factual mappings only; captured source retained for audit, not served publicly.
- [vietnam-factfile](https://assets.publishing.service.gov.uk/media/6a3a740deaee00074150f25f/Vietnam_Toponymic_Factfile.pdf) — retrieved 2026-11-14T17:54:32.315982+00:00; Factual mappings only; captured source retained for audit, not served publicly.
- [astana-city-decree](https://www.akorda.kz/ru/o-pereimenovanii-goroda-nur-sultana-stolicy-respubliki-kazahstan-v-gorod-astanu-stolicu-respubliki-kazahstan-1782457) — retrieved 2026-11-14T17:54:19.673982+00:00; Factual mappings only; captured source retained for audit, not served publicly.
- [za-factfile](https://assets.publishing.service.gov.uk/media/698dcb6843eb912f2e15b351/South_Africa_toponymic_factfile.pdf) — retrieved 2026-11-14T17:54:19.673196+00:00; Factual mappings only; captured source retained for audit, not served publicly.
- [country-timeline](https://www.gov.uk/government/publications/country-names/timeline-of-country-name-changes-in-hmg-use-1919-to-present) — retrieved 2026-11-14T17:52:17.949846+00:00; Factual mappings only; captured source retained for audit, not served publicly.
- [prayagraj-history](https://prayagrajdivision.nic.in/about-department/introduction/) — retrieved 2026-11-14T17:57:23.415657+00:00; Factual mappings only; captured source retained for audit, not served publicly.
- [Ukrposhta city address classifier: Самар](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80) — retrieved 2026-11-14T18:33:43.268213+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta city address classifier: Шахтарське](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%A8%D0%B0%D1%85%D1%82%D0%B0%D1%80%D1%81%D1%8C%D0%BA%D0%B5) — retrieved 2026-11-14T18:33:43.739657+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta city address classifier: Сокологірськ](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%A1%D0%BE%D0%BA%D0%BE%D0%BB%D0%BE%D0%B3%D1%96%D1%80%D1%81%D1%8C%D0%BA) — retrieved 2026-11-14T18:33:44.210869+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta city address classifier: Отаманівка](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%9E%D1%82%D0%B0%D0%BC%D0%B0%D0%BD%D1%96%D0%B2%D0%BA%D0%B0) — retrieved 2026-11-14T18:33:44.662333+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta city address classifier: Сіверськодонецьк](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%A1%D1%96%D0%B2%D0%B5%D1%80%D1%81%D1%8C%D0%BA%D0%BE%D0%B4%D0%BE%D0%BD%D0%B5%D1%86%D1%8C%D0%BA) — retrieved 2026-11-14T18:33:45.094830+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta city address classifier: Шептицький](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%A8%D0%B5%D0%BF%D1%82%D0%B8%D1%86%D1%8C%D0%BA%D0%B8%D0%B9) — retrieved 2026-11-14T18:33:45.492956+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta city address classifier: Хутір-Михайлівський](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%A5%D1%83%D1%82%D1%96%D1%80-%D0%9C%D0%B8%D1%85%D0%B0%D0%B9%D0%BB%D1%96%D0%B2%D1%81%D1%8C%D0%BA%D0%B8%D0%B9) — retrieved 2026-11-14T18:33:45.934340+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta city address classifier: Берестин](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%91%D0%B5%D1%80%D0%B5%D1%81%D1%82%D0%B8%D0%BD) — retrieved 2026-11-14T18:33:46.468385+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta city address classifier: Златопіль](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%97%D0%BB%D0%B0%D1%82%D0%BE%D0%BF%D1%96%D0%BB%D1%8C) — retrieved 2026-11-14T18:33:46.923484+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta city address classifier: Багачеве](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%91%D0%B0%D0%B3%D0%B0%D1%87%D0%B5%D0%B2%D0%B5) — retrieved 2026-11-14T18:33:47.356729+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta city address classifier: Підгороднє](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%9F%D1%96%D0%B4%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BD%D1%94) — retrieved 2026-11-14T18:33:47.781359+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta city address classifier: Південне](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%9F%D1%96%D0%B2%D0%B4%D0%B5%D0%BD%D0%BD%D0%B5) — retrieved 2026-11-14T18:33:48.210857+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.
- [Ukrposhta city address classifier: Південноукраїнськ](https://index.ukrposhta.ua/endpoints-for-apps/index.php?method=get_city_by_region_id_and_district_id_and_city_ua&city_ua=%D0%9F%D1%96%D0%B2%D0%B4%D0%B5%D0%BD%D0%BD%D0%BE%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA) — retrieved 2026-11-14T18:33:48.645179+00:00; Factual address-name mappings only; source response retained for audit, not served publicly.

## Gaps

### Ukraine
- Current national directory and Kyiv street register not reconciled; Kharkiv includes the 48 street entries of order 513 В (26 July 2024) plus non-overlapping postal-classifier mappings; full legal-history and geometry reconciliation remains incomplete
- Postal-classifier captures supplement the cities listed in this report; other municipalities and complete historical rename chains remain gaps
- Lviv appendix 2 recovered: 118 published mappings; 10 Lviv/Briukhovychi rows held for municipal-decision reconciliation
### Poland
- TERYT/ULIC current-register comparison not completed; Łódź has 151 reviewed mappings, including historical chains and current-register checks for the 46 additions; not its full historical inventory
- Wrocław historical pairs checked against municipal EMUiA name/type inventory; boundaries and house numbers remain unverified. Poznań, Gdańsk, Szczecin, Katowice, Lublin and Białystok remain gaps
### South Africa
- No municipal GIS geometry imported; Cape Town coverage is limited to eight unambiguous mappings; conflicting Lansdowne segments held for review; Pretoria includes the visitor map table with Church Street segments preserved
- Ekurhuleni, Mangaung, Msunduzi, Buffalo City, Nelson Mandela Bay and other municipalities remain gaps
- Durban combined streets and suspicious spellings held for review
### Vietnam
- Ho Chi Minh City: officially confirmed partial rename plus independently corroborated historical entries; remaining historical leads held for review
- Đà Nẵng resolution 66/2024 inspected: new roads and bridge names, not genuine street renames; excluded
- Hanoi source leads mostly new naming, length changes or drafts; not published as renames
- Huế, Hải Phòng, Cần Thơ and other municipalities not imported; historical Saigon table not reconciled
### Kazakhstan
- Almaty, Astana and Shymkent decisions imported; no GIS reconciliation
- Karaganda, Pavlodar, Aktobe, Kostanay, Semey, Öskemen, Taraz, Atyrau and other municipalities not imported
### India
- Delhi historical decisions imported, proposals excluded; Chennai pending text verification; Kolkata has one municipal-newsletter mapping, with the partial Moore Avenue lead held for review
- Mumbai, Bengaluru, Hyderabad, Pune, Ahmedabad and other municipalities not imported
- British Council historical table not imported; newer municipal registers not systematically compared
### Uzbekistan
- Tashkent directory mappings only; legal decisions, current national register and geometry not reconciled. Numbered lanes are separate source objects; ambiguous and partial mappings held.
### Lithuania
- Vilnius historical names only; current-name existence cross-checked against an address-register-derived road inventory. Ambiguous labels and unmatched destinations withheld; historical geometry, complete legal chains and other Lithuanian municipalities remain gaps.
### Czechia
- Brno profiles from the first 18 alphabetic index pages; remaining profiles and other cities not imported. Abolished streets and combined labels excluded. Full legal histories and geometry remain unverified.
### Moldova
- Chișinău: unambiguous pairs from the 2017 municipal-library guide, checked against its contemporary street index. Later changes, legal chains, geometry and other Moldovan cities remain unverified.
### Estonia
- Tallinn: whole-street renames from the EKI 2018 snapshot, checked against its 2018 street inventory. Partial streets, later changes and other Estonian municipalities remain gaps.

## Limits

- No exhaustive national coverage claim.
- Postal-classifier imports establish explicit previous/current name pairs at capture time; dates, legal decisions and complete historical chains are not supplied.
- Map links are name searches, not verified geometries or coordinates.
- No house-number carryover claimed.
- Current national registers and OSM object history not reconciled.
- Historical district names are retained from source documents.
- Interface translations generated in this run; native-speaker review pending.
- OCR automation and general GIS reconciliation not implemented; unclear rows excluded.
- Public deployment accessibility, custom-domain DNS and search-console ownership must be checked separately; repository SEO settings do not establish live indexing.

## Languages

en, uk, ru, pl, vi, zu, kk, hi, mr, bn, ta

## Sample searches

Горького, Kyiv; Lecha Kaczyńskiego, Warsaw; Smith Street, Durban; Xa lo Ha Noi, Saigon; Юрия Гагарина, Алматы; Aurangzeb Road, Delhi.

Machine-readable source failures and review records are in data/coverage-report.json.
