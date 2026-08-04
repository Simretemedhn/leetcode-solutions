class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]
        result = []
        
        def backtrack(idx, hour_sum, minute_sum, leds_used, is_hour):
            # If we've used exactly 'turnedOn' LEDs
            if leds_used == turnedOn:
                # Valid time check
                if hour_sum <= 11 and minute_sum <= 59:
                    result.append(f"{hour_sum}:{minute_sum:02d}")
                return
            
            # If we've processed all LEDs
            if idx >= len(hours) + len(minutes):
                return
            
            # Determine if current index is in hours or minutes
            if idx < len(hours):  # Hour LED
                hour_val = hours[idx]
                # EXCLUDE: Don't turn on this LED
                backtrack(idx + 1, hour_sum, minute_sum, leds_used, True)
                # INCLUDE: Turn on this LED
                if hour_sum + hour_val <= 11:
                    backtrack(idx + 1, hour_sum + hour_val, minute_sum, leds_used + 1, True)
            else:  # Minute LED
                minute_idx = idx - len(hours)
                minute_val = minutes[minute_idx]
                # EXCLUDE: Don't turn on this LED
                backtrack(idx + 1, hour_sum, minute_sum, leds_used, False)
                # INCLUDE: Turn on this LED
                if minute_sum + minute_val <= 59:
                    backtrack(idx + 1, hour_sum, minute_sum + minute_val, leds_used + 1, False)
        
        backtrack(0, 0, 0, 0, True)
        return result