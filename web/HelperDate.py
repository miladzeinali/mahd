"""
Created by Abbas Dehghanzadeh on 1397/09/19
"""
from persiantools.jdatetime import JalaliDate
import datetime, pytz


class HelperDate :
    # //this fields are in gregorian format
    # public $date = null;
    # private $year = null;
    # private $month = null;
    # private $day = null;

    """
    @param string when is Date you want,this param shold be in this format:Y/m/d
    @param bool jalaliFormat if be true means that when has given to jalali foramt
    """
    def __init__(self, when = 'now', jalaliFormat = True, splitor = '/'):
        if when != 'now':
            date = when.split(splitor)
            for i in range(len(date)):
                date[i] = int(date[i])
            if jalaliFormat:
                self.j_date = JalaliDate(date[0], date[1], date[2])
                self.g_date = self.j_date.to_gregorian()
            elif not jalaliFormat:
                self.g_date = datetime.date(date[0], date[1], date[2])
                self.j_date = JalaliDate(self.g_date)
        else:
            self.j_date = JalaliDate.today()
            self.g_date = self.j_date.to_gregorian()

    """
    @param string $format declare that you want output in what format
    @param bool $jalaliFormat,if be true means that you wnat output in jalali calendar
    @return array|string, tarikh of this object in string
    """
    def get_date(self, format = '%Y/%m/%d', jalaliFormat = True):
        if jalaliFormat:
            return self.j_date.strftime(format)
        else:
            return self.g_date.strftime(format)

    def get_number_of_week(self):
        return ((int)(self.g_date.strftime('%u'))+1)%7

    def get_number_of_year(self):
        return (int)(self.j_date.strftime('%j'))

    def get_persian_month_in_string(self):
        return self.get_date()[5:7]

    def get_persian_year(self):
        return self.get_date()[0:4]

    def add_day(self,number_of_days=1):
        self.j_date = self.j_date + datetime.timedelta(days=number_of_days)
        self.g_date = self.g_date + datetime.timedelta(days=number_of_days)

    def sub_day(self,number_of_days=1):
        self.j_date = self.j_date - datetime.timedelta(days=number_of_days)
        self.g_date = self.g_date - datetime.timedelta(days=number_of_days)

#     /**
#     * @param int $day
#                   * this method adds to this tarikh days
#                                                     */
#                                                     public function addDay($day=1){
#     $this->date->add(new DateInterval('P'.$day.'D'));
#     $this->updateFields();
#     }
#
#     /**
#     * @param int $day
#                   * this method sub from this tarikh days
#                                                      */
#                                                      public function subDay($day=1){
#     $this->date->sub(new DateInterval('P'.$day.'D'));
#     $this->updateFields();
#     }
#
#     /**
#     * @param int $month
#                   * this method sub from this tarikh days
#                                                      */
#                                                      public function subMonth($month=1){
#     $this->date->sub(new DateInterval('P'.$month.'M'));
#     $this->updateFields();
#     }
#
#     //get name of monthes
#     public function getPersianMonthName(){
#     $date=$this->getDate();
#     $monthNumber=intval(substr($date,5,2));
#     switch ($monthNumber){
#         case 1:
#     $monthName = 'فروردین';
#     break;
#     case 2:
#     $monthName = 'اردیبهشت';
#     break;
#     case 3:
#     $monthName = 'خرداد';
#     break;
#     case 4:
#     $monthName = 'تیر';
#     break;
#     case 5:
#     $monthName = 'مرداد';
#     break;
#     case 6:
#     $monthName = 'شهریور';
#     break;
#     case 7:
#     $monthName = 'مهر';
#     break;
#     case 8:
#     $monthName = 'آبان';
#     break;
#     case 9:
#     $monthName = 'آذر';
#     break;
#     case 10:
#     $monthName = 'دی';
#     break;
#     case 11:
#     $monthName = 'بهمن';
#     break;
#     default:
#     $monthName = 'اسفند';
#     break;
#     }
#     return $monthName;
#     }
#
#     //get Number of month
#     public function getPersianMonthNumber(){
#     $date=$this->getDate();
#     $monthNumber=intval(substr($date,5,2));
#     return $monthNumber;
#     }
#
#     //get Number of month in string format
#     public function getPersianMonthNumberInString(){
#     $date=$this->getDate();
#     $monthNumber=intval(substr($date,5,2));
#     return $monthNumber<10?'0'.$monthNumber:$monthNumber;
#     }
#
    def get_persian_day_name(self):
        day_number = self.get_number_of_week()
        names = ['شنبه', 'یکشنبه', 'دوشنبه', 'سه شنبه', 'چهارشنبه', 'پنجشنبه', 'جمعه']
        return names[day_number];

#
#     //return that this date is what day number in week
#     public function getNumberOfWeek(){
#     return intval($this->date->format('N'));
#     }
#
#     //get Number of day
#     public function getPersianDayNumber(){
#     $date=$this->getDate();
#     $dayNumber=intval(substr($date,8,2));
#     return $dayNumber;
#     }
#
#     //get Number of year
#     public function getPersianYear(){
#     $date=$this->getDate();
#     $dayNumber=intval(substr($date,0,4));
#     return $dayNumber;
#     }
#
#     /**
#     * update fields from tarikh
#     */
#     private function updateFields() {
#     sscanf($this->getDate('Y/m/d',false), "%d/%d/%d", $this->year, $this->month, $this->day);
#     }
#
# }