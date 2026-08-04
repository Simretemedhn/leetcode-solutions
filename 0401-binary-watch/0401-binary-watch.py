class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hour = [1, 2, 4, 8]
        minute = [1, 2, 4, 8, 16, 32]
        res = []

        def backtracking(h_i, m_i, chosen_hour, chosen_minute):
            # If we've selected exactly turnedOn LEDs, check if valid
            if len(chosen_hour) + len(chosen_minute) == turnedOn:
                hour_sum = sum(chosen_hour)
                minute_sum = sum(chosen_minute)   
                
                # Check if hour and minute are valid            
                if hour_sum <= 11 and minute_sum <= 59:
                    minute_str = f"{minute_sum:02d}"  # Always 2 digits with leading zero
                    hour_str = str(hour_sum)
                    res.append(f"{hour_str}:{minute_str}")
                return        
            
            # If we've exceeded turnedOn LEDs, stop
            if len(chosen_hour) + len(chosen_minute) > turnedOn:
                return 
            
            # If we've gone through all hour and minute LEDs
            if h_i >= len(hour) and m_i >= len(minute):
                return
            
            # Try selecting an hour LED       
            if h_i < len(hour):    
                # Option 1: Select this hour LED
                hour_sum = sum(chosen_hour)
                if hour_sum + hour[h_i] <= 11:
                    chosen_hour.append(hour[h_i])
                    backtracking(h_i + 1, m_i, chosen_hour, chosen_minute)
                    chosen_hour.pop()
                
                # Option 2: Skip this hour LED
                backtracking(h_i + 1, m_i, chosen_hour, chosen_minute)
            
            # Try selecting a minute LED   
            elif m_i < len(minute):
                # Option 1: Select this minute LED
                minute_sum = sum(chosen_minute)
                if minute_sum + minute[m_i] <= 59:
                    chosen_minute.append(minute[m_i])
                    backtracking(h_i, m_i + 1, chosen_hour, chosen_minute)
                    chosen_minute.pop()
                
                # Option 2: Skip this minute LED
                backtracking(h_i, m_i + 1, chosen_hour, chosen_minute)
        
        backtracking(0, 0, [], [])
        return sorted(res)  # Optional: sort for consistent output


"""class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hour = [1, 2, 4, 8]
        minute = [1, 2, 4, 8, 16, 32]
        res = []

        def backtracking(h_i, m_i, chosen_hour, chosen_minute):
            if len(chosen_hour) + len(chosen_minute) == turnedOn:
                hour_sum = sum(chosen_hour)
                minute_sum = sum(chosen_minute)
                if minute_sum < 10:
                    minute_str = f"0{minute_sum}"
                else:
                    minute_str = str(minute_sum)
                hour_str = str(hour_sum)
                res.append(f"{hour_str}:{minute_str}")
                return
            if len(chosen_hour) + len(chosen_minute) > turnedOn:
                return 
            # Choose an hour LED
            if h_i < len(hour):
                hour_sum = sum(chosen_hour)
                if hour_sum + hour[h_i] <= 11:
                    chosen_hour.append(hour[h_i])
                    backtracking(h_i + 1, m_i, chosen_hour, chosen_minute)
                    chosen_hour.pop()
                
                # Option to skip this hour LED
                backtracking(h_i + 1, m_i, chosen_hour, chosen_minute)
            
            # Choose a minute LED
            if m_i < len(minute):
                minute_sum = sum(chosen_minute)
                if minute_sum + minute[m_i] <= 59:
                    chosen_minute.append(minute[m_i])
                    backtracking(h_i, m_i + 1, chosen_hour, chosen_minute)
                    chosen_minute.pop()
                
                # Option to skip this minute LED
                backtracking(h_i, m_i + 1, chosen_hour, chosen_minute)
        
        backtracking(0, 0, [], [])
        return res


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hour = [1, 2, 4, 8]
        minute = [1, 2, 4, 8, 16, 32]
        res = []

        def backtracking(h_i, m_i, choosen_hour, choosen_minute):
            if used_hour + used_minute == turnedOn:
                hour = sum(choosen_hour)
                minute = sum(choosen_minute) 
                if minute < 10:
                    minute = f"0{minute}"
                hour = str(hour)
                res.append(f"{hour}:{minute}")
            
            if sum(choosen_hour) + hour[i] <= 12:
                choosen_hour.append(hour[i])
                backtracking(h_i + 1, m_i, choosen_hour, choosen_minute)
                choosen_hour.pop()
            
            if sum(choosen_minute) + minute[i] <= 60 and len(choosen_hour) + len(choosen_minute) + 1 <= turnedOn:
                choosen_minute.append(minute[i])
                backtracking(h_i, m_i+1, choosen_hour, choosen_minute)\
                choosen_hour.pop()
        
        backtracking(0, 0, [], [])
        return res"""