import { CommonModule, DatePipe } from '@angular/common';
import { Component, OnInit, ChangeDetectionStrategy, ChangeDetectorRef } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthenticationService } from '../_services/authentication/authentication.service';

@Component({
  selector: 'app-word-of-the-day',
  templateUrl: './word-of-the-day.component.html',
  styleUrls: ['./word-of-the-day.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [CommonModule],
  providers: [DatePipe]
})
export class WordOfTheDayComponent implements OnInit {

  definition$: Observable<any>;
  
  fullDate: string | null;

  constructor(private _authService: AuthenticationService, private datePipe: DatePipe, private _cd: ChangeDetectorRef) { 

    const myDate = new Date();
    this.fullDate = this.datePipe.transform(myDate, 'EEEE, MMMM d, y');
  }

  ngOnInit() {
    this._authService.getRandomWord().subscribe(word => {
      console.log(word);

      this._authService.getDefinition(word).subscribe(def => {
        console.log(def[0]);
        
        if (def[0].meta) {
          this.definition$ = this._authService.getDefinition(word);
        } else {
          this.definition$ = this._authService.getDefinition(def[0]);
        }

        this._cd.markForCheck();
      });

    });
  }
}
