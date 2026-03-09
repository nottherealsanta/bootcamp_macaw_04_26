import requests
import concurrent.futures
import time
import random

# Base URL of your FastAPI server
BASE_URL = "http://localhost:8000/predict"

# Sample car data templates
def generate_sample_data():
    """Generate random but realistic car data for testing"""
    return {
        "Mileage_km": random.uniform(10000, 200000),
        "Year": random.randint(2015, 2024),
        "Fuel_Consumption_l": round(random.uniform(4.0, 12.0), 1),
        "Gears": random.choice([5, 6, 7, 8, 9]),
        "Power_hp": random.randint(80, 500),
        "Engine_Size_cc": random.randint(1000, 5000),
        "Cylinders": random.choice([3, 4, 6, 8]),
        "Seats": random.choice([2, 4, 5, 7]),
        "Doors": random.choice([2, 3, 4, 5]),
        "Previous_Owners": random.randint(0, 3)
    }

def make_request(request_id):
    """Make a single POST request to the prediction endpoint"""
    data = generate_sample_data()
    
    start_time = time.time()
    try:
        response = requests.post(BASE_URL, json=data)
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        
        if response.status_code == 200:
            result = response.json()
            print(f"Request {request_id}: SUCCESS - Predicted Price: {result.get('predicted_price', 'N/A'):.2f} (Time: {elapsed_time:.3f}s)")
            return {
                "request_id": request_id,
                "status": "success",
                "response": result,
                "time": elapsed_time,
                "data_sent": data
            }
        else:
            print(f"Request {request_id}: FAILED - Status: {response.status_code} (Time: {elapsed_time:.3f}s)")
            return {
                "request_id": request_id,
                "status": "failed",
                "status_code": response.status_code,
                "time": elapsed_time
            }
    except Exception as e:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Request {request_id}: ERROR - {str(e)} (Time: {elapsed_time:.3f}s)")
        return {
            "request_id": request_id,
            "status": "error",
            "error": str(e),
            "time": elapsed_time
        }

def run_concurrent_requests(num_requests=100):
    """Run multiple requests concurrently using ThreadPoolExecutor"""
    print(f"\n{'='*60}")
    print(f"Starting {num_requests} concurrent requests...")
    print(f"{'='*60}\n")
    
    start_time = time.time()
    
    # Use ThreadPoolExecutor to run requests concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_requests) as executor:
        # Submit all requests
        futures = [executor.submit(make_request, i+1) for i in range(num_requests)]
        
        # Wait for all requests to complete
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    
    end_time = time.time()
    total_time = end_time - start_time
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"{'='*60}")
    
    successful = sum(1 for r in results if r['status'] == 'success')
    failed = sum(1 for r in results if r['status'] == 'failed')
    errors = sum(1 for r in results if r['status'] == 'error')
    
    print(f"Total requests: {num_requests}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Errors: {errors}")
    print(f"Total time: {total_time:.3f}s")
    print(f"Average time per request: {total_time/num_requests:.3f}s")
    
    if successful > 0:
        avg_response_time = sum(r['time'] for r in results if r['status'] == 'success') / successful
        print(f"Average successful response time: {avg_response_time:.3f}s")
    
    return results

if __name__ == "__main__":
    # Run 10 concurrent requests
    run_concurrent_requests(1000)
    
    
    # Optionally, you can adjust the number of requests
    # results = run_concurrent_requests(20)