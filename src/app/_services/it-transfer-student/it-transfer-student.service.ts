import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map, Observable } from 'rxjs';
import { ITTransferStudent } from 'src/app/_models/it-transfer-student.model';

@Injectable({
  providedIn: 'root'
})
export class ItTransferStudentService {

  constructor(private _http: HttpClient) { }


  getBooks(): Observable<ITTransferStudent[]> {
    return this._http
      .get<{ items: ITTransferStudent[] }>(
        'https://www.googleapis.com/books/v1/volumes?maxResults=5&orderBy=relevance&q=oliver%20sacks'
      )
      .pipe(
        map((books) => books.items || []));
  }
}
