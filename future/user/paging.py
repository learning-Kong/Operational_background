#自定义分页模块

from django.utils.safestring import mark_safe

class Page:
    def __init__(self, current_page, data_count, per_page, page_num):
        self.current_page = current_page
        self.data_count = data_count
        self.per_page = per_page
        self.page_num = page_num
    def start(self):
        return (self.current_page - 1) * self.per_page

    def end(self):
        return self.current_page * self.per_page

    @property
    def total_count(self):
        quotient, remainder = divmod(self.data_count, self.per_page)
        if remainder:
            quotient += 1
        return quotient
    def page_str(self):
        page_list = []

        #分情况处理分页的起始，终止页码ID
        if self.total_count < self.page_num:
            start_index = 1
            end_index = self.total_count + 1
        else:
            if self.current_page <= (self.page_num + 1) / 2:
                start_index = 1
                end_index = self.page_num + 1
            else:
                start_index = self.current_page - (self.page_num + 1) / 2
                end_index = self.current_page + (self.page_num + 1) / 2
                if (self.current_page + (self.page_num + 1) / 2) > total_count:
                    start_index = total_count - self.page_num + 1
                    end_index = total_count + 1

        #分情况处理上一页跳转情况
        if self.current_page == 1:
            prev = '''
                <li class="paginate_button">
                    <a href="javascript:void(0);" aria-controls="example2" data-dt-idx="0" tabindex="0">上一页</a>
                </li>
            '''
        else:
            prev = '''
                <li class="paginate_button">
                    <a href="/user/change/?p=%s" aria-controls="example2" data-dt-idx="0" tabindex="0">上一页</a>
                </li>
            ''' % (self.current_page - 1,)
        page_list.append(prev)

        #处理页码跳转
        for i in range(int(start_index), int(end_index)):
            if i == self.current_page:
                temp = '''
                    <li class="paginate_button active">
                        <a href="/user/change/?p=%s" aria-controls="example2" data-dt-idx="0" tabindex="0">%s</a>
                    </li>
                ''' % (i, i)
            else:
                temp = '''
                    <li class="paginate_button">
                        <a href="/user/change/?p=%s" aria-controls="example2" data-dt-idx="0" tabindex="0">%s</a>
                    </li>
                ''' % (i, i)
            page_list.append(temp)

        # 分情况处理下一页跳转情况
        if self.current_page == self.total_count:
            jump = '''
                <li class="paginate_button">
                    <a href="javascript:void(0);" aria-controls="example2" data-dt-idx="0" tabindex="0">下一页</a>
                </li>
            '''
        else:
            jump = '''
                <li class="paginate_button">
                    <a href="/user/change/?p=%s" aria-controls="example2" data-dt-idx="0" tabindex="0">下一页</a>
                </li>
            ''' % (self.current_page + 1,)
        page_list.append(jump)

        #设置为安全
        page_str = mark_safe("".join(page_list))

        return page_str