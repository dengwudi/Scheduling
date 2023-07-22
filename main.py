#手动输入数据
import datetime
# # 班次定义
# shifts = {
#     '8B': {'time_range': '8:15-16:00', 'end_time': '16:00'},
#     '8C': {'time_range': '8:30-17:30', 'end_time': '17:30'},
#     '9A': {'time_range': '9:15-16:30', 'end_time': '16:30'},
#     '9B': {'time_range': '9:30-18:00', 'end_time': '18:00'},
#     '7A': {'time_range': '7:45-15:45', 'end_time': '15:45'},
#     '16A': {'time_range': '16:00-23:00', 'end_time': '23:00'},
#     '16B': {'time_range': '16:30-23:00', 'end_time': '23:00'},
#     '17B': {'time_range': '17:00-23:30', 'end_time': '23:30'},
#     '办1': {'time_range': '8:30-16:30', 'end_time': '16:30'},
#     '19A': {'time_range': '19:15-2:00', 'end_time': '2:00'},
#     'C1': {'time_range': '22:10-8:30', 'end_time': '8:30'},
#     'C': {'time_range': '21:45-8:15', 'end_time': '8:15'},
#     '专A': {'time_range': '7:30-15:30', 'end_time': '15:30'},
#     '专B': {'time_range': '15:30-22:00', 'end_time': '22:00'},
#     '17A': {'time_range': '17:45-00:30', 'end_time': '00:30'}
# }
#
# # 员工信息
# employees = {}
#
# # 座位信息
# studio302_seats = [
#     "3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
#     "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4",
#     "3B—5—1", "3B—5—2", "3B—5—3", "3B—5—4", "3B—6—1", "3B—6—2", "3B—6—3", "3B—6—4",
#     "3B—7—1", "3B—7—2", "3B—7—3", "3B—7—4", "3B—8—1", "3B—8—2", "3B—8—3", "3B—8—4",
#     "3B—9—1", "3B—9—2", "3B—9—3", "3B—9—4", "3B—9—5", "3B—9—6", "3B—10—1", "3B—10—2",
#     "3B—10—3", "3B—10—4", "3B—10—5", "3B—10—6", "3B—11—1", "3B—11—2", "3B—11—3",
#     "3B—11—4", "3B—11—5", "3B—12—1", "3B—12—2", "3B—12—3", "3B—12—4", "3B—12—5",
#     "3B—13—1", "3B—13—2", "3B—13—3", "3B—13—4", "3B—13—5", "3B—13—6", "3B—14—1",
#     "3B—14—2", "3B—14—3", "3B—14—4", "3B—14—5", "3B—14—6", "3B—15—1", "3B—15—2",
#     "3B—15—3", "3B—15—4", "3B—15—5", "3B—16—1", "3B—16—2", "3B—16—3", "3B—16—4",
#     "3B—16—5", "3B—17—1", "3B—17—2", "3B—17—3", "3B—17—4", "3B—17—5", "3B—17—6",
#     "3B—18—1", "3B—18—2", "3B—18—3", "3B—18—4", "3B—18—5", "3B—18—6", "3B—19—1",
#     "3B—19—2", "3B—19—3", "3B—19—4", "3B—19—5", "3B—20—1", "3B—20—2", "3B—20—3",
#     "3B—20—4", "3B—20—5", "3B—21—1", "3B—21—2", "3B—21—3", "3B—21—4", "3B—21—5"
#
# ]
#
# studio402_seats = [
#     "4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2", "4B—4—3",
#     "4B—5—1", "4B—5—2", "4B—5—3", "4B—6—1", "4B—6—2", "4B—6—3", "4B—7—1", "4B—7—2",
#     "4B—7—3", "4B—8—1", "4B—8—2", "4B—8—3", "4B—8—4", "4B—9—1", "4B—9—2", "4B—9—3",
#     "4B—9—4", "4B—9—5", "4B—9—6", "4B—10—1", "4B—10—2", "4B—10—3", "4B—10—4", "4B—10—5",
#     "4B—10—6", "4B—11—1", "4B—11—2", "4B—11—3", "4B—11—4", "4B—11—5", "4B—12—1",
#     "4B—12—2", "4B—12—3", "4B—12—4", "4B—12—5", "4B—13—1", "4B—13—2", "4B—13—3",
#     "4B—13—4", "4B—13—5", "4B—13—6", "4B—14—1", "4B—14—2", "4B—14—3", "4B—14—4",
#     "4B—14—5", "4B—14—6", "4B—15—1", "4B—15—2", "4B—15—3", "4B—15—4", "4B—15—5",
#     "4B—16—1", "4B—16—2", "4B—16—3", "4B—16—4", "4B—16—5", "4B—17—1", "4B—17—2",
#     "4B—17—3", "4B—17—4", "4B—17—5", "4B—17—6", "4B—18—1", "4B—18—2", "4B—18—3",
#     "4B—18—4", "4B—18—5", "4B—18—6", "4B—19—1", "4B—19—2", "4B—19—3", "4B—19—4",
#     "4B—19—5", "4B—20—1", "4B—20—2", "4B—20—3", "4B—20—4", "4B—20—5", "4B—21—1",
#     "4B—21—2", "4B—21—3", "4B—21—4", "4B—21—5"
# ]
#
# seats = {
#     "studio302": [False] * len(studio302_seats),
#     "studio402": [False] * len(studio402_seats),
# }
#
# # 座位使用情况
# seats_usage = {}
#
#
# # 新增分配优先级的座位信息
# priority_seats = {
#     "实习": ("studio302", ["3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
#                            "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4"]),
#     "专A": ("studio402", ["4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2"]),
#     "专B": ("studio402", ["4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2"]),
# }
#
# # 解析时间
# def parse_time(time_str):
#     return datetime.datetime.strptime(time_str, "%H:%M").time()
#
#
# # 检查座位使用情况
# def check_seat_usage(employee_name):
#     shift = employees[employee_name]["shift"]
#     shift_end = parse_time(shifts[shift]["end_time"])
#
#     # 如果当前时间在班次结束时间之后，那么座位应该已经空闲
#     if shift_end <= datetime.time(0, 0):
#         if employee_name in seats_usage:
#             studio, seat = seats_usage[employee_name]
#             seats[studio][seat] = False
#             del seats_usage[employee_name]
#
#
# # 分配座位并打印分配结果
# def assign_seat(employee_name):
#     # 获取员工的班次和组名
#     shift = employees[employee_name]["shift"]
#     group = employees[employee_name]["group"]
#
#     # 检查员工是否有优先级座位可以分配
#     if group in priority_seats or shift in priority_seats:
#         priority_seat_info = priority_seats.get(group) or priority_seats.get(shift)
#         studio, studio_seats = priority_seat_info
#
#         for i, seat_name in enumerate(studio_seats):
#             # 如果找到空座位，就分配给该员工
#             if not seats[studio][i]:
#                 seats[studio][i] = True
#                 seats_usage[employee_name] = (studio, i)
#                 print(f"{seat_name}\t{group}\t{employee_name}\t{shift}")
#                 return
#
#     # 如果没有找到优先级座位或者优先级座位都被分配完了，就按照原来的逻辑分配座位
#     for studio, studio_seats in seats.items():
#         for i, seat in enumerate(studio_seats):
#             if not seat:
#                 studio_seats[i] = True
#                 seats_usage[employee_name] = (studio, i)
#                 print(f"{globals()[studio + '_seats'][i]}\t{group}\t{employee_name}\t{shift}")
#                 return
#
#     # 如果所有座位都被分配完了，就打印一个消息
#     print(f"员工{employee_name}没有可用的座位")
#
#
# # 定义排序的优先级
# group_priority = {
#     "专A": 0,
#     "专B": 1,
#     "实习": 2,
# }
#
# # 读取输入并排序
# def read_input():
#     global employees  # 将employees声明为全局变量
#     print("请粘贴组信息，每行一个组。每个组信息包括组名称、员工姓名和班次，用空格或制表符分隔。输入完毕后，直接按回车键结束输入。\n")
#     employees = {}
#
#     while True:
#         line = input()
#         if not line.strip():
#             break
#         parts = line.split('\t')
#         if len(parts) != 3:
#             print("输入的数据格式不正确，请重新输入。")
#             continue
#         group, name, shift = parts
#         employees[name] = {"group": group, "shift": shift}
#
#     return employees
#
# def main():
#     # 读取输入并排序
#     read_input()
#     sorted_employees = sorted(employees.items(),
#     key=lambda x: (group_priority.get(x[1]['group'], 3), shifts[x[1]['shift']]['end_time']))
#     print("座位\t班组\t姓名\t班次")  # 输出标题行
#     # 按照排序后的员工列表进行座位分配
#     for employee_name, employee_info in sorted_employees:
#         assign_seat(employee_name)
#         check_seat_usage(employee_name)
#
# if __name__ == "__main__":
#     main()
#























# 从excel表中读取数据
# 从excel表中读取数据
# import pandas as pd
# import datetime
#
#
# # 班次定义
# shifts = {
#     '8B': {'time_range': '8:15-16:00', 'end_time': '16:00'},
#     '8C': {'time_range': '8:30-17:30', 'end_time': '17:30'},
#     '9A': {'time_range': '9:15-16:30', 'end_time': '16:30'},
#     '9B': {'time_range': '9:30-18:00', 'end_time': '18:00'},
#     '7A': {'time_range': '7:45-15:45', 'end_time': '15:45'},
#     '16A': {'time_range': '16:00-23:00', 'end_time': '23:00'},
#     '16B': {'time_range': '16:30-23:00', 'end_time': '23:00'},
#     '17B': {'time_range': '17:00-23:30', 'end_time': '23:30'},
#     '办1': {'time_range': '8:30-16:30', 'end_time': '16:30'},
#     '19A': {'time_range': '19:15-2:00', 'end_time': '2:00'},
#     'C1': {'time_range': '22:10-8:30', 'end_time': '8:30'},
#     'C': {'time_range': '21:45-8:15', 'end_time': '8:15'},
#     '专A': {'time_range': '7:30-15:30', 'end_time': '15:30'},
#     '专B': {'time_range': '15:30-22:00', 'end_time': '22:00'},
#     '17A': {'time_range': '17:45-00:30', 'end_time': '00:30'}
# }
#
# # 员工信息
# employees = {}
#
# # 座位信息
# studio302_seats = [
#     "3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
#     "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4",
#     "3B—5—1", "3B—5—2", "3B—5—3", "3B—5—4", "3B—6—1", "3B—6—2", "3B—6—3", "3B—6—4",
#     "3B—7—1", "3B—7—2", "3B—7—3", "3B—7—4", "3B—8—1", "3B—8—2", "3B—8—3", "3B—8—4",
#     "3B—9—1", "3B—9—2", "3B—9—3", "3B—9—4", "3B—9—5", "3B—9—6", "3B—10—1", "3B—10—2",
#     "3B—10—3", "3B—10—4", "3B—10—5", "3B—10—6", "3B—11—1", "3B—11—2", "3B—11—3",
#     "3B—11—4", "3B—11—5", "3B—12—1", "3B—12—2", "3B—12—3", "3B—12—4", "3B—12—5",
#     "3B—13—1", "3B—13—2", "3B—13—3", "3B—13—4", "3B—13—5", "3B—13—6", "3B—14—1",
#     "3B—14—2", "3B—14—3", "3B—14—4", "3B—14—5", "3B—14—6", "3B—15—1", "3B—15—2",
#     "3B—15—3", "3B—15—4", "3B—15—5", "3B—16—1", "3B—16—2", "3B—16—3", "3B—16—4",
#     "3B—16—5", "3B—17—1", "3B—17—2", "3B—17—3", "3B—17—4", "3B—17—5", "3B—17—6",
#     "3B—18—1", "3B—18—2", "3B—18—3", "3B—18—4", "3B—18—5", "3B—18—6", "3B—19—1",
#     "3B—19—2", "3B—19—3", "3B—19—4", "3B—19—5", "3B—20—1", "3B—20—2", "3B—20—3",
#     "3B—20—4", "3B—20—5", "3B—21—1", "3B—21—2", "3B—21—3", "3B—21—4", "3B—21—5"
# ]
#
# studio402_seats = [
#     "4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2", "4B—4—3",
#     "4B—5—1", "4B—5—2", "4B—5—3", "4B—6—1", "4B—6—2", "4B—6—3", "4B—7—1", "4B—7—2",
#     "4B—7—3", "4B—8—1", "4B—8—2", "4B—8—3", "4B—8—4", "4B—9—1", "4B—9—2", "4B—9—3",
#     "4B—9—4", "4B—9—5", "4B—9—6", "4B—10—1", "4B—10—2", "4B—10—3", "4B—10—4", "4B—10—5",
#     "4B—10—6", "4B—11—1", "4B—11—2", "4B—11—3", "4B—11—4", "4B—11—5", "4B—12—1",
#     "4B—12—2", "4B—12—3", "4B—12—4", "4B—12—5", "4B—13—1", "4B—13—2", "4B—13—3",
#     "4B—13—4", "4B—13—5", "4B—13—6", "4B—14—1", "4B—14—2", "4B—14—3", "4B—14—4",
#     "4B—14—5", "4B—14—6", "4B—15—1", "4B—15—2", "4B—15—3", "4B—15—4", "4B—15—5",
#     "4B—16—1", "4B—16—2", "4B—16—3", "4B—16—4", "4B—16—5", "4B—17—1", "4B—17—2",
#     "4B—17—3", "4B—17—4", "4B—17—5", "4B—17—6", "4B—18—1", "4B—18—2", "4B—18—3",
#     "4B—18—4", "4B—18—5", "4B—18—6", "4B—19—1", "4B—19—2", "4B—19—3", "4B—19—4",
#     "4B—19—5", "4B—20—1", "4B—20—2", "4B—20—3", "4B—20—4", "4B—20—5", "4B—21—1",
#     "4B—21—2", "4B—21—3", "4B—21—4", "4B—21—5"
# ]
#
# seats = {
#     "studio302": [False] * len(studio302_seats),
#     "studio402": [False] * len(studio402_seats),
# }
#
# # 座位使用情况
# seats_usage = {}
#
#
# # 新增分配优先级的座位信息
# priority_seats = {
#     "实习实习谭银球组": ("studio302", ["3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
#                            "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4"]),
#     "实习梁紫琪组": ("studio302", ["3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
#                                        "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4"]),
#     "实习梅美弦组": ("studio302", ["3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
#                                        "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4"]),
#     "专业1组": ("studio402", ["4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2"]),
#     "专业2组": ("studio402", ["4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2"]),
# }
#
# # 解析时间
# def parse_time(time_str):
#     return datetime.datetime.strptime(time_str, "%H:%M").time()
#
# # 初始化等待分配座位的队列
# waiting_queue = []
# end_time_waiting_queue = []
#
# # 新员工进入时，将其添加到等待分配座位的队列中
# def add_to_waiting_queue(employee_name):
#     waiting_queue.append(employee_name)
#
# # 员工的工作时间结束时，将其占用的座位标记为空闲状态
# def release_seat(employee_name):
#     if employee_name in seats_usage:
#         studio, seat = seats_usage[employee_name]
#         seats[studio][seat] = False
#         del seats_usage[employee_name]
#
# # 检查座位使用情况
# def check_seat_usage(employee_name):
#     shift = employees[employee_name]["shift"]
#     shift_end = parse_time(shifts[shift]["end_time"])
#
#     # 如果当前时间在班次结束时间之后，那么座位应该已经空闲
#     if datetime.datetime.now().time() >= shift_end:
#         release_seat(employee_name)
#     else:
#         if employee_name in seats_usage:
#             end_time_waiting_queue.append(employee_name)
#         else:
#             add_to_waiting_queue(employee_name)
#
#
#
# # 分配座位并打印分配结果
# def assign_seat(employee_name):
#     # 获取员工的班次和组名
#     shift = employees[employee_name]["shift"]
#     group = employees[employee_name]["group"]
#
#     # 检查员工是否有优先级座位可以分配
#     if group in priority_seats or shift in priority_seats:
#         priority_seat_info = priority_seats.get(group) or priority_seats.get(shift)
#         studio, studio_seats = priority_seat_info
#
#         for i, seat_name in enumerate(studio_seats):
#             # 如果找到空座位，就分配给该员工
#             if not seats[studio][i]:
#                 seats[studio][i] = True
#                 seats_usage[employee_name] = (studio, i)
#                 print(f"{seat_name}\t{group}\t{employee_name}\t{shift}")
#                 return
#
#     # 如果没有找到优先级座位或者优先级座位都被分配完了，就按照原来的逻辑分配座位
#     for studio, studio_seats in seats.items():
#         for i, seat in enumerate(studio_seats):
#             if not seat:
#                 studio_seats[i] = True
#                 seats_usage[employee_name] = (studio, i)
#                 print(f"{globals()[studio + '_seats'][i]}\t{group}\t{employee_name}\t{shift}")
#                 return
#
#     # 如果所有座位都被分配完了，就打印一个消息
#     print(f"员工{employee_name}没有可用的座位")
#
#
#
#
# # 定义排序的优先级
# group_priority = {
#     "专业1组": 0,
#     "专业2组": 0,
#     "实习谭银球组": 0,
#     "实习梁紫琪组": 0,
#     "实习梅美弦组": 0,
# }
#
#
#
#
# # 从Excel文档中读取员工数据
# def read_input_from_excel(file_path):
#     global employees
#     employees = {}
#     df = pd.read_excel(file_path)
#     for index, row in df.iterrows():
#         group = row["组名"]
#         name = row["姓名"]
#         shift = row["班次"]
#         employees[name] = {"group": group, "shift": shift}
#
#     return employees
#
# def main():
#     # 读取输入并排序
#     file_path = "00718上班名单.xlsx"  # 修改为您的Excel文件路径
#     read_input_from_excel(file_path)
#     sorted_employees = sorted(employees.items(),
#     key=lambda x: (group_priority.get(x[1]['group'], 3), parse_time(shifts[x[1]['shift']]['end_time'])))
#
#     print("座位\t班组\t姓名\t班次")  # 输出标题行
#
#     # 检查并释放座位，分配座位并打印分配结果
#     for employee_name, employee_info in sorted_employees:
#         check_seat_usage(employee_name)
#         if employee_name in waiting_queue:
#             assign_seat(employee_name)
#
#
# if __name__ == "__main__":
#     main()



















# # 从excel表中读取数据
# import pandas as pd
# import datetime
#
# # 班次定义
# shifts = {
#     '8B': {'time_range': '8:15-16:00', 'end_time': '16:00'},
#     '8C': {'time_range': '8:30-17:30', 'end_time': '17:30'},
#     '9A': {'time_range': '9:15-16:30', 'end_time': '16:30'},
#     '9B': {'time_range': '9:30-18:00', 'end_time': '18:00'},
#     '7A': {'time_range': '7:45-15:45', 'end_time': '15:45'},
#     '16A': {'time_range': '16:00-23:00', 'end_time': '23:00'},
#     '16B': {'time_range': '16:30-23:00', 'end_time': '23:00'},
#     '17B': {'time_range': '17:00-23:30', 'end_time': '23:30'},
#     '办1': {'time_range': '8:30-16:30', 'end_time': '16:30'},
#     '19A': {'time_range': '19:15-2:00', 'end_time': '2:00'},
#     'C1': {'time_range': '22:10-8:30', 'end_time': '8:30'},
#     'C': {'time_range': '21:45-8:15', 'end_time': '8:15'},
#     '专A': {'time_range': '7:30-15:30', 'end_time': '15:30'},
#     '专B': {'time_range': '15:30-22:00', 'end_time': '22:00'},
#     '17A': {'time_range': '17:45-00:30', 'end_time': '00:30'}
# }
#
# # 员工信息
# employees = {}
#
# # 座位信息
# studio302_seats = [
#     "3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
#     "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4",
#     "3B—5—1", "3B—5—2", "3B—5—3", "3B—5—4", "3B—6—1", "3B—6—2", "3B—6—3", "3B—6—4",
#     "3B—7—1", "3B—7—2", "3B—7—3", "3B—7—4", "3B—8—1", "3B—8—2", "3B—8—3", "3B—8—4",
#     "3B—9—1", "3B—9—2", "3B—9—3", "3B—9—4", "3B—9—5", "3B—9—6", "3B—10—1", "3B—10—2",
#     "3B—10—3", "3B—10—4", "3B—10—5", "3B—10—6", "3B—11—1", "3B—11—2", "3B—11—3",
#     "3B—11—4", "3B—11—5", "3B—12—1", "3B—12—2", "3B—12—3", "3B—12—4", "3B—12—5",
#     "3B—13—1", "3B—13—2", "3B—13—3", "3B—13—4", "3B—13—5", "3B—13—6", "3B—14—1",
#     "3B—14—2", "3B—14—3", "3B—14—4", "3B—14—5", "3B—14—6", "3B—15—1", "3B—15—2",
#     "3B—15—3", "3B—15—4", "3B—15—5", "3B—16—1", "3B—16—2", "3B—16—3", "3B—16—4",
#     "3B—16—5", "3B—17—1", "3B—17—2", "3B—17—3", "3B—17—4", "3B—17—5", "3B—17—6",
#     "3B—18—1", "3B—18—2", "3B—18—3", "3B—18—4", "3B—18—5", "3B—18—6", "3B—19—1",
#     "3B—19—2", "3B—19—3", "3B—19—4", "3B—19—5", "3B—20—1", "3B—20—2", "3B—20—3",
#     "3B—20—4", "3B—20—5", "3B—21—1", "3B—21—2", "3B—21—3", "3B—21—4", "3B—21—5"
# ]
#
# studio402_seats = [
#     "4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2", "4B—4—3",
#     "4B—5—1", "4B—5—2", "4B—5—3", "4B—6—1", "4B—6—2", "4B—6—3", "4B—7—1", "4B—7—2",
#     "4B—7—3", "4B—8—1", "4B—8—2", "4B—8—3", "4B—8—4", "4B—9—1", "4B—9—2", "4B—9—3",
#     "4B—9—4", "4B—9—5", "4B—9—6", "4B—10—1", "4B—10—2", "4B—10—3", "4B—10—4", "4B—10—5",
#     "4B—10—6", "4B—11—1", "4B—11—2", "4B—11—3", "4B—11—4", "4B—11—5", "4B—12—1",
#     "4B—12—2", "4B—12—3", "4B—12—4", "4B—12—5", "4B—13—1", "4B—13—2", "4B—13—3",
#     "4B—13—4", "4B—13—5", "4B—13—6", "4B—14—1", "4B—14—2", "4B—14—3", "4B—14—4",
#     "4B—14—5", "4B—14—6", "4B—15—1", "4B—15—2", "4B—15—3", "4B—15—4", "4B—15—5",
#     "4B—16—1", "4B—16—2", "4B—16—3", "4B—16—4", "4B—16—5", "4B—17—1", "4B—17—2",
#     "4B—17—3", "4B—17—4", "4B—17—5", "4B—17—6", "4B—18—1", "4B—18—2", "4B—18—3",
#     "4B—18—4", "4B—18—5", "4B—18—6", "4B—19—1", "4B—19—2", "4B—19—3", "4B—19—4",
#     "4B—19—5", "4B—20—1", "4B—20—2", "4B—20—3", "4B—20—4", "4B—20—5", "4B—21—1",
#     "4B—21—2", "4B—21—3", "4B—21—4", "4B—21—5"
# ]
#
# seats = {
#     "studio302": [False] * len(studio302_seats),
#     "studio402": [False] * len(studio402_seats),
# }
#
# # 座位使用情况
# seats_usage = {}
#
# 新增分配优先级的座位信息
# priority_seats = {
#     "实习实习谭银球组": ("studio302", ["3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
#                            "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4"]),
#     "实习梁紫琪组": ("studio302", ["3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
#                                        "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4"]),
#     "实习梅美弦组": ("studio302", ["3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
#                                        "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4"]),
#     "专业1组": ("studio402", ["4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2"]),
#     "专业2组": ("studio402", ["4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2"]),
# }
#
# # 解析时间
# def parse_time(time_str):
#     return datetime.datetime.strptime(time_str, "%H:%M").time()
#
# # 初始化等待分配座位的队列
# waiting_queue = []
# end_time_waiting_queue = []
#
# # 新员工进入时，将其添加到等待分配座位的队列中
# def add_to_waiting_queue(employee_name):
#     waiting_queue.append(employee_name)
#
# # 员工的工作时间结束时，将其占用的座位标记为空闲状态
# def release_seat(employee_name):
#     if employee_name in seats_usage:
#         studio, seat = seats_usage[employee_name]
#         seats[studio][seat] = False
#         del seats_usage[employee_name]
#
# # 检查座位使用情况
# def check_seat_usage(employee_name):
#     if employee_name in seats_usage:
#         end_time_waiting_queue.append(employee_name)
#     else:
#         add_to_waiting_queue(employee_name)
#
# # 分配座位并打印分配结果
# def assign_seat(employee_name):
#     # 获取员工的班次和组名
#     shift = employees[employee_name]["shift"]
#     group = employees[employee_name]["group"]
#
#     # 检查员工是否有优先级座位可以分配
#     if group in priority_seats or shift in priority_seats:
#         priority_seat_info = priority_seats.get(group) or priority_seats.get(shift)
#         studio, studio_seats = priority_seat_info
#
#         for i, seat_name in enumerate(studio_seats):
#             # 如果找到空座位，就分配给该员工
#             if not seats[studio][i]:
#                 seats[studio][i] = True
#                 seats_usage[employee_name] = (studio, i)
#                 print(f"{seat_name}\t{group}\t{employee_name}\t{shift}")
#                 return
#
#     # 如果没有找到优先级座位或者优先级座位都被分配完了，就按照原来的逻辑分配座位
#     for studio, studio_seats in seats.items():
#         for i, seat in enumerate(studio_seats):
#             if not seat:
#                 studio_seats[i] = True
#                 seats_usage[employee_name] = (studio, i)
#                 print(f"{globals()[studio + '_seats'][i]}\t{group}\t{employee_name}\t{shift}")
#                 return
#
#     # 如果所有座位都被分配完了，就打印一个消息
#     print(f"员工{employee_name}没有可用的座位")
#
# # 定义排序的优先级
# group_priority = {
#     "专业1组": 0,
#     "专业2组": 0,
#     "实习谭银球组": 0,
#     "实习梁紫琪组": 0,
#     "实习梅美弦组": 0,
# }
#
# # 从Excel文档中读取员工数据
# def read_input_from_excel(file_path):
#     global employees
#     employees = {}
#     df = pd.read_excel(file_path)
#     for index, row in df.iterrows():
#         group = row["组名"]
#         name = row["姓名"]
#         shift = row["班次"]
#         employees[name] = {"group": group, "shift": shift}
#
#     return employees
#
# def main():
#     # 读取输入并排序
#     file_path = "00718上班名单.xlsx"  # 修改为您的Excel文件路径
#     read_input_from_excel(file_path)
#     sorted_employees = sorted(employees.items(),
#     key=lambda x: (group_priority.get(x[1]['group'], 3), parse_time(shifts[x[1]['shift']]['end_time'])))
#
#     print("座位\t班组\t姓名\t班次")  # 输出标题行
#
#     # 检查并释放座位，分配座位并打印分配结果
#     for employee_name, employee_info in sorted_employees:
#         check_seat_usage(employee_name)
#         if employee_name in waiting_queue:
#             assign_seat(employee_name)
#
# if __name__ == "__main__":
#     main()













    # # 从excel表中读取数据
    # import pandas as pd
    # import datetime
    #
    # # 班次定义
    # shifts = {
    #     '8B': {'time_range': '8:15-16:00', 'end_time': '16:00'},
    #     '8C': {'time_range': '8:30-17:30', 'end_time': '17:30'},
    #     '9A': {'time_range': '9:15-16:30', 'end_time': '16:30'},
    #     '9B': {'time_range': '9:30-18:00', 'end_time': '18:00'},
    #     '7A': {'time_range': '7:45-15:45', 'end_time': '15:45'},
    #     '16A': {'time_range': '16:00-23:00', 'end_time': '23:00'},
    #     '16B': {'time_range': '16:30-23:00', 'end_time': '23:00'},
    #     '17B': {'time_range': '17:00-23:30', 'end_time': '23:30'},
    #     '办1': {'time_range': '8:30-16:30', 'end_time': '16:30'},
    #     '19A': {'time_range': '19:15-2:00', 'end_time': '2:00'},
    #     'C1': {'time_range': '22:10-8:30', 'end_time': '8:30'},
    #     'C': {'time_range': '21:45-8:15', 'end_time': '8:15'},
    #     '专A': {'time_range': '7:30-15:30', 'end_time': '15:30'},
    #     '专B': {'time_range': '15:30-22:00', 'end_time': '22:00'},
    #     '17A': {'time_range': '17:45-00:30', 'end_time': '00:30'}
    # }
    #
    # # 员工信息
    # employees = {}
    #
    # # 座位信息
    # studio302_seats = [
    #     "3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
    #     "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4",
    #     "3B—5—1", "3B—5—2", "3B—5—3", "3B—5—4", "3B—6—1", "3B—6—2", "3B—6—3", "3B—6—4",
    #     "3B—7—1", "3B—7—2", "3B—7—3", "3B—7—4", "3B—8—1", "3B—8—2", "3B—8—3", "3B—8—4",
    #     "3B—9—1", "3B—9—2", "3B—9—3", "3B—9—4", "3B—9—5", "3B—9—6", "3B—10—1", "3B—10—2",
    #     "3B—10—3", "3B—10—4", "3B—10—5", "3B—10—6", "3B—11—1", "3B—11—2", "3B—11—3",
    #     "3B—11—4", "3B—11—5", "3B—12—1", "3B—12—2", "3B—12—3", "3B—12—4", "3B—12—5",
    #     "3B—13—1", "3B—13—2", "3B—13—3", "3B—13—4", "3B—13—5", "3B—13—6", "3B—14—1",
    #     "3B—14—2", "3B—14—3", "3B—14—4", "3B—14—5", "3B—14—6", "3B—15—1", "3B—15—2",
    #     "3B—15—3", "3B—15—4", "3B—15—5", "3B—16—1", "3B—16—2", "3B—16—3", "3B—16—4",
    #     "3B—16—5", "3B—17—1", "3B—17—2", "3B—17—3", "3B—17—4", "3B—17—5", "3B—17—6",
    #     "3B—18—1", "3B—18—2", "3B—18—3", "3B—18—4", "3B—18—5", "3B—18—6", "3B—19—1",
    #     "3B—19—2", "3B—19—3", "3B—19—4", "3B—19—5", "3B—20—1", "3B—20—2", "3B—20—3",
    #     "3B—20—4", "3B—20—5", "3B—21—1", "3B—21—2", "3B—21—3", "3B—21—4", "3B—21—5"
    # ]
    #
    # studio402_seats = [
    #     "4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2", "4B—4—3",
    #     "4B—5—1", "4B—5—2", "4B—5—3", "4B—6—1", "4B—6—2", "4B—6—3", "4B—7—1", "4B—7—2",
    #     "4B—7—3", "4B—8—1", "4B—8—2", "4B—8—3", "4B—8—4", "4B—9—1", "4B—9—2", "4B—9—3",
    #     "4B—9—4", "4B—9—5", "4B—9—6", "4B—10—1", "4B—10—2", "4B—10—3", "4B—10—4", "4B—10—5",
    #     "4B—10—6", "4B—11—1", "4B—11—2", "4B—11—3", "4B—11—4", "4B—11—5", "4B—12—1",
    #     "4B—12—2", "4B—12—3", "4B—12—4", "4B—12—5", "4B—13—1", "4B—13—2", "4B—13—3",
    #     "4B—13—4", "4B—13—5", "4B—13—6", "4B—14—1", "4B—14—2", "4B—14—3", "4B—14—4",
    #     "4B—14—5", "4B—14—6", "4B—15—1", "4B—15—2", "4B—15—3", "4B—15—4", "4B—15—5",
    #     "4B—16—1", "4B—16—2", "4B—16—3", "4B—16—4", "4B—16—5", "4B—17—1", "4B—17—2",
    #     "4B—17—3", "4B—17—4", "4B—17—5", "4B—17—6", "4B—18—1", "4B—18—2", "4B—18—3",
    #     "4B—18—4", "4B—18—5", "4B—18—6", "4B—19—1", "4B—19—2", "4B—19—3", "4B—19—4",
    #     "4B—19—5", "4B—20—1", "4B—20—2", "4B—20—3", "4B—20—4", "4B—20—5", "4B—21—1",
    #     "4B—21—2", "4B—21—3", "4B—21—4", "4B—21—5"
    # ]
    #
    # seats = {
    #     "studio302": [False] * len(studio302_seats),
    #     "studio402": [False] * len(studio402_seats),
    # }
    #
    # # 座位使用情况
    # seats_usage = {}
    #
    # 新增分配优先级的座位信息
    # priority_seats = {
    #     "实习": ("studio302", ["3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
    #                            "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4"]),
    #     "专A": ("studio402", ["4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2"]),
    #     "专B": ("studio402", ["4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2"]),
    # }
    #
    #
    # # 解析时间
    # def parse_time(time_str):
    #     return datetime.datetime.strptime(time_str, "%H:%M").time()
    #
    #
    # # 检查座位使用情况
    # def check_seat_usage(employee_name):
    #     shift = employees[employee_name]["shift"]
    #     shift_end = parse_time(shifts[shift]["end_time"])
    #
    #     # 如果当前时间在班次结束时间之后，那么座位应该已经空闲
    #     if shift_end <= datetime.time(0, 0):
    #         if employee_name in seats_usage:
    #             studio, seat = seats_usage[employee_name]
    #             seats[studio][seat] = False
    #             del seats_usage[employee_name]
    #
    #
    # # 分配座位并打印分配结果
    # def assign_seat(employee_name):
    #     # 获取员工的班次和组名
    #     shift = employees[employee_name]["shift"]
    #     group = employees[employee_name]["group"]
    #
    #     # 检查员工是否有优先级座位可以分配
    #     if group in priority_seats or shift in priority_seats:
    #         priority_seat_info = priority_seats.get(group) or priority_seats.get(shift)
    #         studio, studio_seats = priority_seat_info
    #
    #         for i, seat_name in enumerate(studio_seats):
    #             # 如果找到空座位，就分配给该员工
    #             if not seats[studio][i]:
    #                 seats[studio][i] = True
    #                 seats_usage[employee_name] = (studio, i)
    #                 print(f"{seat_name}\t{group}\t{employee_name}\t{shift}")
    #                 return
    #
    #     # 如果没有找到优先级座位或者优先级座位都被分配完了，就按照原来的逻辑分配座位
    #     for studio, studio_seats in seats.items():
    #         for i, seat in enumerate(studio_seats):
    #             if not seat:
    #                 studio_seats[i] = True
    #                 seats_usage[employee_name] = (studio, i)
    #                 print(f"{globals()[studio + '_seats'][i]}\t{group}\t{employee_name}\t{shift}")
    #                 return
    #
    #     # 如果所有座位都被分配完了，就打印一个消息
    #     print(f"员工{employee_name}没有可用的座位")
    #
    #
    # # 定义排序的优先级
    # group_priority = {
    #     "专A": 0,
    #     "专B": 1,
    #     "实习": 2,
    # }
    #
    #
    # # 从Excel文档中读取员工数据
    # def read_input_from_excel(file_path):
    #     global employees
    #     employees = {}
    #     df = pd.read_excel(file_path)
    #     for index, row in df.iterrows():
    #         group = row["组名"]
    #         name = row["姓名"]
    #         shift = row["班次"]
    #         employees[name] = {"group": group, "shift": shift}
    #
    #     return employees
    #
    #
    # def main():
    #     # 读取输入并排序
    #     file_path = "0718上班名单.xlsx"  # 修改为您的Excel文件路径
    #     read_input_from_excel(file_path)
    #     sorted_employees = sorted(employees.items(),
    #                               key=lambda x: (
    #                               group_priority.get(x[1]['group'], 3), shifts[x[1]['shift']]['end_time']))
    #     print("座位\t班组\t姓名\t班次")  # 输出标题行
    #     # 按照排序后的员工列表进行座位分配
    #     for employee_name, employee_info in sorted_employees:
    #         check_seat_usage(employee_name)
    #         assign_seat(employee_name)
    #         check_seat_usage(employee_name)
    #
    #
    # if __name__ == "__main__":
    #     main()
#













# # 读取输入数据文本并按行拆分数据
# input_data = """
# 组名  姓名    班次
# 专业1组  黄海裕  专A
# 专业1组  黎钰兰  专B
# 专业2组  苏倩文  专B
# ......(此处省略其他数据)......
# 实习梅美弦组  李佩滢  8B
# 实习梅美弦组  李晓轩  8B
# """
#
# lines = input_data.strip().split('\n')
# data = [line.split() for line in lines]
#
# # 创建字典来存储组名及其成员
# groups = {}
#
# # 按组名分类
# for line in data[1:]:
#     group_name, member_name, _ = line
#     if group_name in groups:
#         groups[group_name].append(member_name)
#     else:
#         groups[group_name] = [member_name]
#
# # 输出每个组的成员列表
# for group, members in groups.items():
#     print(f"{group} 组的成员有：")
#     print(', '.join(members))
#     print()
#
# # 输出共有多少个组和成员总数
# total_groups = len(groups)
# total_members = sum(len(members) for members in groups.values())
# print(f"共有 {total_groups} 个组，总共有 {total_members} 个成员。")





# import pandas as pd
# import datetime
#
# class SeatAllocationSystem:
#     def __init__(self):
#         self.shifts = {
#             '8B': {'time_range': '8:15-16:00', 'end_time': '16:00'},
#             '8C': {'time_range': '8:30-17:30', 'end_time': '17:30'},
#             '9A': {'time_range': '9:15-16:30', 'end_time': '16:30'},
#             '9B': {'time_range': '9:30-18:00', 'end_time': '18:00'},
#             '7A': {'time_range': '7:45-15:45', 'end_time': '15:45'},
#             '16A': {'time_range': '16:00-23:00', 'end_time': '23:00'},
#             '16B': {'time_range': '16:30-23:00', 'end_time': '23:00'},
#             '17B': {'time_range': '17:00-23:30', 'end_time': '23:30'},
#             '办1': {'time_range': '8:30-16:30', 'end_time': '16:30'},
#             '19A': {'time_range': '19:15-2:00', 'end_time': '2:00'},
#             'C1': {'time_range': '22:10-8:30', 'end_time': '8:30'},
#             'C': {'time_range': '21:45-8:15', 'end_time': '8:15'},
#             '专A': {'time_range': '7:30-15:30', 'end_time': '15:30'},
#             '专B': {'time_range': '15:30-22:00', 'end_time': '22:00'},
#             '17A': {'time_range': '17:45-00:30', 'end_time': '00:30'}
#         }
#
#         self.employees = {}
#         self.seats = {
#             "studio302": [False] * 105,
#             "studio402": [False] * 105,
#         }
#         self.seats_usage = {}
#         self.priority_seats = {
#             "实习": ("studio302", ["3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
#                                   "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4"]),
#             "专A": ("studio402", ["4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2"]),
#             "专B": ("studio402", ["4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2"]),
#         }
#
#         self.group_priority = {
#             "专A": 0,
#             "专B": 1,
#             "实习": 2,
#         }
#
#     def parse_time(self, time_str):
#         return datetime.datetime.strptime(time_str, "%H:%M").time()
#
#     def read_input_from_excel(self, file_path):
#         self.employees = {}
#         df = pd.read_excel(file_path)
#         for index, row in df.iterrows():
#             group = row["组名"]
#             name = row["姓名"]
#             shift = row["班次"]
#             self.employees[name] = {"group": group, "shift": shift}
#
#     def check_seat_usage(self, employee_name):
#         shift = self.employees[employee_name]["shift"]
#         shift_end = self.parse_time(self.shifts[shift]["end_time"])
#
#         if shift_end <= datetime.time(0, 0):
#             if employee_name in self.seats_usage:
#                 studio, seat = self.seats_usage[employee_name]
#                 self.seats[studio][seat] = False
#                 del self.seats_usage[employee_name]
#
#     def assign_seat(self, employee_name):
#         # 获取员工的班次和组名
#         shift = self.employees[employee_name]["shift"]
#         group = self.employees[employee_name]["group"]
#
#         # 检查员工是否有优先级座位可以分配
#         if group in self.priority_seats or shift in self.priority_seats:
#             priority_seat_info = self.priority_seats.get(group) or self.priority_seats.get(shift)
#             studio, studio_seats = priority_seat_info
#
#             for i, seat_name in enumerate(studio_seats):
#                 # 如果找到空座位，就分配给该员工
#                 if not self.seats[studio][i]:
#                     self.seats[studio][i] = True
#                     self.seats_usage[employee_name] = (studio, i)
#                     print(f"{self.get_seat_name(studio, i)}\t{group}\t{employee_name}\t{shift}")
#                     self.check_seat_usage(employee_name)  # 更新座位状态
#                     return
#
#         # 如果没有找到优先级座位或者优先级座位都被分配完了，就按照原来的逻辑分配座位
#         for studio, studio_seats in self.seats.items():
#             for i, seat in enumerate(studio_seats):
#                 if not seat:
#                     self.seats[studio][i] = True
#                     self.seats_usage[employee_name] = (studio, i)
#                     print(f"{self.get_seat_name(studio, i)}\t{group}\t{employee_name}\t{shift}")
#                     self.check_seat_usage(employee_name)  # 更新座位状态
#                     return
#
#         # 如果所有座位都被分配完了，就打印一个消息
#         print(f"员工{employee_name}没有可用的座位")
#
#     def sort_employees(self):
#         sorted_employees = sorted(self.employees.items(),
#                                   key=lambda x: (self.group_priority.get(x[1]['group'], 3),
#                                                  self.parse_time(self.shifts[x[1]['shift']]['end_time'])))
#         return sorted_employees
#
#     def distribute_seats(self):
#         sorted_employees = self.sort_employees()
#         print("座位\t班组\t姓名\t班次")
#         for employee_name, employee_info in sorted_employees:
#             self.assign_seat(employee_name)
#             self.check_seat_usage(employee_name)
#
#
#     def get_seat_name(self, studio, index):
#         studio302_seats = [
#             "3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
#             "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4",
#             "3B—5—1", "3B—5—2", "3B—5—3", "3B—5—4", "3B—6—1", "3B—6—2", "3B—6—3", "3B—6—4",
#             "3B—7—1", "3B—7—2", "3B—7—3", "3B—7—4", "3B—8—1", "3B—8—2", "3B—8—3", "3B—8—4",
#             "3B—9—1", "3B—9—2", "3B—9—3", "3B—9—4", "3B—9—5", "3B—9—6", "3B—10—1", "3B—10—2",
#             "3B—10—3", "3B—10—4", "3B—10—5", "3B—10—6", "3B—11—1", "3B—11—2", "3B—11—3",
#             "3B—11—4", "3B—11—5", "3B—12—1", "3B—12—2", "3B—12—3", "3B—12—4", "3B—12—5",
#             "3B—13—1", "3B—13—2", "3B—13—3", "3B—13—4", "3B—13—5", "3B—13—6", "3B—14—1",
#             "3B—14—2", "3B—14—3", "3B—14—4", "3B—14—5", "3B—14—6", "3B—15—1", "3B—15—2",
#             "3B—15—3", "3B—15—4", "3B—15—5", "3B—16—1", "3B—16—2", "3B—16—3", "3B—16—4",
#             "3B—16—5", "3B—17—1", "3B—17—2", "3B—17—3", "3B—17—4", "3B—17—5", "3B—17—6",
#             "3B—18—1", "3B—18—2", "3B—18—3", "3B—18—4", "3B—18—5", "3B—18—6", "3B—19—1",
#             "3B—19—2", "3B—19—3", "3B—19—4", "3B—19—5", "3B—20—1", "3B—20—2", "3B—20—3",
#             "3B—20—4", "3B—20—5", "3B—21—1", "3B—21—2", "3B—21—3", "3B—21—4", "3B—21—5"
#         ]
#
#         studio402_seats = [
#             "4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2", "4B—4—3",
#             "4B—5—1", "4B—5—2", "4B—5—3", "4B—6—1", "4B—6—2", "4B—6—3", "4B—7—1", "4B—7—2",
#             "4B—7—3", "4B—8—1", "4B—8—2", "4B—8—3", "4B—8—4", "4B—9—1", "4B—9—2", "4B—9—3",
#             "4B—9—4", "4B—9—5", "4B—9—6", "4B—10—1", "4B—10—2", "4B—10—3", "4B—10—4", "4B—10—5",
#             "4B—10—6", "4B—11—1", "4B—11—2", "4B—11—3", "4B—11—4", "4B—11—5", "4B—12—1",
#             "4B—12—2", "4B—12—3", "4B—12—4", "4B—12—5", "4B—13—1", "4B—13—2", "4B—13—3",
#             "4B—13—4", "4B—13—5", "4B—13—6", "4B—14—1", "4B—14—2", "4B—14—3", "4B—14—4",
#             "4B—14—5", "4B—14—6", "4B—15—1", "4B—15—2", "4B—15—3", "4B—15—4", "4B—15—5",
#             "4B—16—1", "4B—16—2", "4B—16—3", "4B—16—4", "4B—16—5", "4B—17—1", "4B—17—2",
#             "4B—17—3", "4B—17—4", "4B—17—5", "4B—17—6", "4B—18—1", "4B—18—2", "4B—18—3",
#             "4B—18—4", "4B—18—5", "4B—18—6", "4B—19—1", "4B—19—2", "4B—19—3", "4B—19—4",
#             "4B—19—5", "4B—20—1", "4B—20—2", "4B—20—3", "4B—20—4", "4B—20—5", "4B—21—1",
#             "4B—21—2", "4B—21—3", "4B—21—4", "4B—21—5"
#         ]
#
#         if studio == "studio302":
#             return studio302_seats[index]
#         elif studio == "studio402":
#             return studio402_seats[index]
#         else:
#             return f"{studio}—{index}"
#
#
#
# if __name__ == "__main__":
#     seat_allocation_system = SeatAllocationSystem()
#     seat_allocation_system.read_input_from_excel("0718上班名单.xlsx")
#     seat_allocation_system.distribute_seats()















# 从excel表中读取数据
import pandas as pd
import datetime
from openpyxl import load_workbook
from datetime import time, timedelta

# 班次定义
shifts = {
    '8B': {'time_range': '8:15-16:00', 'end_time': '16:00'},
    '8C': {'time_range': '8:30-17:30', 'end_time': '17:30'},
    '9A': {'time_range': '9:15-16:30', 'end_time': '16:30'},
    '9B': {'time_range': '9:30-18:00', 'end_time': '18:00'},
    '7A': {'time_range': '7:45-15:45', 'end_time': '15:45'},
    '16A': {'time_range': '16:00-23:00', 'end_time': '23:00'},
    '16B': {'time_range': '16:30-23:00', 'end_time': '23:00'},
    '17B': {'time_range': '17:00-23:30', 'end_time': '23:30'},
    '办1': {'time_range': '8:30-16:30', 'end_time': '16:30'},
    '19A': {'time_range': '19:15-2:00', 'end_time': '2:00'},
    'C1': {'time_range': '22:10-8:30', 'end_time': '8:30'},
    'C': {'time_range': '21:45-8:15', 'end_time': '8:15'},
    '专A': {'time_range': '7:30-15:30', 'end_time': '15:30'},
    '专B': {'time_range': '15:30-22:00', 'end_time': '22:00'},
    '17A': {'time_range': '17:45-00:30', 'end_time': '00:30'}
}

# 员工信息
employees = {}

# 座位信息
studio302_seats = [
    "3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
    "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4",
    "3B—5—1", "3B—5—2", "3B—5—3", "3B—5—4", "3B—6—1", "3B—6—2", "3B—6—3", "3B—6—4",
    "3B—7—1", "3B—7—2", "3B—7—3", "3B—7—4", "3B—8—1", "3B—8—2", "3B—8—3", "3B—8—4",
    "3B—9—1", "3B—9—2", "3B—9—3", "3B—9—4", "3B—9—5", "3B—9—6", "3B—10—1", "3B—10—2",
    "3B—10—3", "3B—10—4", "3B—10—5", "3B—10—6", "3B—11—1", "3B—11—2", "3B—11—3",
    "3B—11—4", "3B—11—5", "3B—12—1", "3B—12—2", "3B—12—3", "3B—12—4", "3B—12—5",
    "3B—13—1", "3B—13—2", "3B—13—3", "3B—13—4", "3B—13—5", "3B—13—6", "3B—14—1",
    "3B—14—2", "3B—14—3", "3B—14—4", "3B—14—5", "3B—14—6", "3B—15—1", "3B—15—2",
    "3B—15—3", "3B—15—4", "3B—15—5", "3B—16—1", "3B—16—2", "3B—16—3", "3B—16—4",
    "3B—16—5", "3B—17—1", "3B—17—2", "3B—17—3", "3B—17—4", "3B—17—5", "3B—17—6",
    "3B—18—1", "3B—18—2", "3B—18—3", "3B—18—4", "3B—18—5", "3B—18—6", "3B—19—1",
    "3B—19—2", "3B—19—3", "3B—19—4", "3B—19—5", "3B—20—1", "3B—20—2", "3B—20—3",
    "3B—20—4", "3B—20—5", "3B—21—1", "3B—21—2", "3B—21—3", "3B—21—4", "3B—21—5"
]

studio402_seats = [
    "4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2", "4B—4—3",
    "4B—5—2", "4B—5—3", "4B—6—1", "4B—6—2", "4B—6—3", "4B—7—1", "4B—7—2",
    "4B—7—3", "4B—8—1", "4B—8—2", "4B—8—3", "4B—8—4", "4B—9—1", "4B—9—2", "4B—9—3",
    "4B—9—4", "4B—9—5", "4B—9—6", "4B—10—1", "4B—10—2", "4B—10—3", "4B—10—4", "4B—10—5",
    "4B—10—6", "4B—11—1", "4B—11—2", "4B—11—3", "4B—11—4", "4B—11—5", "4B—12—1",
    "4B—12—2", "4B—12—3", "4B—12—4", "4B—12—5", "4B—13—1", "4B—13—2", "4B—13—3",
    "4B—13—4", "4B—13—5", "4B—13—6", "4B—14—1", "4B—14—2", "4B—14—3", "4B—14—4",
    "4B—14—5", "4B—14—6", "4B—15—1", "4B—15—2", "4B—15—3", "4B—15—4", "4B—15—5",
    "4B—16—1", "4B—16—2", "4B—16—3", "4B—16—4", "4B—16—5", "4B—17—1", "4B—17—2",
    "4B—17—3", "4B—17—4", "4B—17—5", "4B—17—6", "4B—18—1", "4B—18—2", "4B—18—3",
    "4B—18—4", "4B—18—5", "4B—18—6", "4B—19—1", "4B—19—2", "4B—19—3", "4B—19—4",
    "4B—19—5", "4B—20—1", "4B—20—2", "4B—20—3", "4B—20—4", "4B—20—5", "4B—21—1",
    "4B—21—2", "4B—21—3", "4B—21—4", "4B—21—5",
    # Move "办1" and "8C" to studio402_seats
    "办1",
    "8C"
]


seats = {
    "studio302": [False] * len(studio302_seats),
    "studio402": [False] * len(studio402_seats),
}

# 座位使用情况
seats_usage = {}


# 新增分配优先级的座位信息
priority_seats = {
    "实习谭银球": ("studio302", ["3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
                    "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4"]),
    "实习梁紫琪": ("studio302", ["3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
                   "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4"]),
    "实习梅美弦组": ("studio302", ["3B—1—1", "3B—1—2", "3B—1—3", "3B—1—4", "3B—2—1", "3B—2—2", "3B—2—3", "3B—2—4",
                   "3B—3—1", "3B—3—2", "3B—3—3", "3B—3—4", "3B—4—1", "3B—4—2", "3B—4—3", "3B—4—4"]),
    "专业1组": ("studio402", ["4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2"]),
    "专业2组": ("studio402", ["4B—2—1", "4B—2—2", "4B—3—1", "4B—3—2", "4B—3—3", "4B—4—1", "4B—4—2"]),
}

# 解析时间，考虑跨越午夜的情况
def parse_time(time_str):
    if time_str.endswith("24:00"):
        time_str = time_str.replace("24:00", "23:59")
    return datetime.datetime.strptime(time_str, "%H:%M").time()

# 检查座位使用情况
def check_seat_usage(employee_name):
    shift = employees[employee_name]["shift"]
    shift_end = parse_time(shifts[shift]["end_time"])

    # 如果当前时间在班次结束时间之后，那么座位应该已经空闲
    if shift_end <= datetime.time(0, 0):
        if employee_name in seats_usage:
            studio, seat = seats_usage[employee_name]
            seats[studio][seat] = False
            del seats_usage[employee_name]


# 分配座位并打印分配结果
def assign_seat(employee_name):
    # 获取员工的班次和组名
    shift = employees[employee_name]["shift"]
    group = employees[employee_name]["group"]

    # 检查员工是否有优先级座位可以分配
    if group in priority_seats or shift in priority_seats:
        priority_seat_info = priority_seats.get(group) or priority_seats.get(shift)
        studio, studio_seats = priority_seat_info

        for i, seat_name in enumerate(studio_seats):
            # 如果找到空座位，就分配给该员工
            if not seats[studio][i]:
                seats[studio][i] = True
                seats_usage[employee_name] = (studio, i)
                print(f"{seat_name}\t{group}\t{employee_name}\t{shift}")
                return

    # 如果没有找到优先级座位或者优先级座位都被分配完了，就按照原来的逻辑分配座位
    for studio, studio_seats in seats.items():
        for i, seat in enumerate(studio_seats):
            if not seat:
                studio_seats[i] = True
                seats_usage[employee_name] = (studio, i)
                print(f"{globals()[studio + '_seats'][i]}\t{group}\t{employee_name}\t{shift}")
                return

    # 如果所有座位都被分配完了，就打印一个消息
    print(f"员工{employee_name}没有可用的座位")


# 定义排序的优先级
group_priority = {
    "专业1组": 0,
    "专业2组": 0,
    "实习谭银球": 0,
    "实习梁紫琪": 0,
    "实习梅美弦组": 0,
}

def remaining_time(t):
    end_of_day = time(23, 59, 59)
    delta = timedelta(hours=end_of_day.hour - t.hour, minutes=end_of_day.minute - t.minute, seconds=end_of_day.second - t.second)
    return delta

def sort_shifts(shifts):
    sorted_shifts = sorted(shifts.items(), key=lambda x: (parse_time(x[1]["time_range"].split("-")[0]), remaining_time(parse_time(x[1]["end_time"]))))
    return sorted_shifts

# 从Excel文档中读取员工数据
def read_input_from_excel(file_path):
    global employees
    employees = {}
    df = pd.read_excel(file_path)
    for index, row in df.iterrows():
        group = row["组名"]
        name = row["姓名"]
        shift = row["班次"]
        employees[name] = {"group": group, "shift": shift}

    return employees

def main():
    # 读取输入并排序
    file_path = "00718上班名单.xlsx"  # 修改为您的Excel文件路径
    read_input_from_excel(file_path)
    sorted_employees = sorted(employees.items(),
    key=lambda x: (group_priority.get(x[1]['group'], 3), shifts[x[1]['shift']]['end_time']))
    print("座位\t班组\t姓名\t班次")  # 输出标题行
    # 按照排序后的员工列表进行座位分配
    for employee_name, employee_info in sorted_employees:
        assign_seat(employee_name)
        check_seat_usage(employee_name)

if __name__ == "__main__":
    main()

