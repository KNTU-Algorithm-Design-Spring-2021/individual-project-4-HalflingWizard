<div dir="rtl">

# شرکت پست
##### محمد نامورپور - 9920354
##### تیر 1400 - طراحی الگوریتم دکتر احمدی

<p align="center">
  <img src="https://cdn1.bbcode0.com/uploads/2021/7/3/39fadb384314b7edebddfc8abb9f5d1d-full.jpg" />
</p>

### فایل ها
فایل `main.py` حاوی الگوریتم پیشنهادی به صورت حریصانه می باشد.
  
### روش کار
اول همه وزن ها را مرتب می کنیم. بعد از بزرگترین وزن شروع میکنیم و درون یک کامیون قرار می دهیم. در هر مرحله، هر وزن را که برمیداریم، مقدار آن را با وزن حال حاضر تمام کامیون ها جمع میکنیم و هر کامیون که کمترین وزن را پس از اضافه کردن وزن بار دارد، آن وزن جدید را نیز دریافت خواهد کرد. یعنی در هر مرحله وزن را طوری اضافه میکنیم که مقدار ماکزیمم وزن کامیون ها کمینه شود. و امید داریم که در مجموع مراحل نیز چنین باشد.

### پیچیدگی برنامه
در این الگوریتم یک حلقه `while` داریم که به تعداد وزن ها تکرار می شود. یک حلقه `for` هم داریم که درون حلقه `while` است و هر بار به تعداد کامیون ها تکرار می شود. پس اگر تعداد کامیون ها `k` و تعداد وزن ها `w` باشد، پیچیدگی کد نوشته شده `O(wk)` است.

### نمونه خروجی برنامه

<img src="https://cdn1.bbcode0.com/uploads/2021/7/3/9429d1a556dda548077dedecb481e1fe-full.png" />

</div>