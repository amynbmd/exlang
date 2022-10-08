import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  OnInit,
} from '@angular/core';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { SharedModule } from '../_modules/shared.module';
import { BaseComponent } from '../_shared/BaseComponent';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [SharedModule, MatProgressBarModule],
})
export class HomeComponent extends BaseComponent implements OnInit {
  constructor(
    private _cd: ChangeDetectorRef
  ) {
    super();
  }

  ngOnInit() {

  }
}
