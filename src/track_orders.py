import statistics as st


class TrackOrders:
    def __init__(self):
        self.__consumed = list()

    def __len__(self):
        return len(self.__consumed)

    def add_new_order(self, customer, order, day):
        self.__consumed.append([customer, order, day])
        return self.__consumed

    def get_most_ordered_dish_per_customer(self, customer):
        return st.mode(
            [item[1] for item in self.__consumed if item[0] == customer]
        )

    def get_never_ordered_per_customer(self, customer):
        list = set([item[1] for item in self.__consumed])
        return list.difference(
            set([item[1] for item in self.__consumed if item[0] == customer])
        )

    def get_days_never_visited_per_customer(self, customer):
        days = set([item[2] for item in self.__consumed])
        return days.difference(
            set([item[2] for item in self.__consumed if item[0] == customer])
        )

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
