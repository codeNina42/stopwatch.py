import time

def stopwatch():
    print("simple console stopwatch")
    print("press ctrl+c to stop")

    
    start_time = time.perf_counter()

    try:
        while True:
            
            elapsed = time.perf_counter() - start_time

            
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            milliseconds = int((elapsed - int(elapsed)) * 1000)

          
            print(f"\r{minutes:02d}:{seconds:02d}.{milliseconds:03d}", end="")
            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\nStopped.")
        print(f"Final time: {minutes:02d}:{seconds:02d}.{milliseconds:03d}")


if __name__ == "__main__":
    stopwatch()
