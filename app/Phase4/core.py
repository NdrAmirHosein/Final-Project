from app.Phase4.get_driver_license_date import get_driver_license_date
from app.Phase4.stock_span_algorithm import calculateSpan
from app.data_structures.heap import maxHeap
def phase4_core():
    sorted_license_dates = get_driver_license_date()
    scores = calculateSpan(sorted_license_dates)
    for i in range(len(scores)):
        sorted_license_dates[i].score = scores[i]
    rankink = maxHeap().build_max_heap(sorted_license_dates)

    return rankink
